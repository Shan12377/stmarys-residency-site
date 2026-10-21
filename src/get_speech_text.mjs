// Collects the exact read-aloud text of every built page (same code the Listen button uses).
// Usage: node src/get_speech_text.mjs public out.json   (needs Playwright)
import http from 'http'; import fs from 'fs'; import path from 'path'; import { chromium } from 'playwright';
const [root, out] = process.argv.slice(2);
const SKIP = /^(log|app_build_spec|404|00_start_here)\.html$|^tools\/|^tags\//i;
const pages = [];
(function walk(d) { for (const f of fs.readdirSync(path.join(root, d))) {
  const rel = path.join(d, f); const st = fs.statSync(path.join(root, rel));
  if (st.isDirectory()) walk(rel); else if (f.endsWith('.html') && !SKIP.test(rel) && fs.readFileSync(path.join(root, rel), 'utf8').includes('<article')) pages.push(rel);
} })('');
const srv = http.createServer((q, r) => { let p = decodeURIComponent(q.url.split('?')[0]); if (p.endsWith('/')) p += 'index'; let f = path.join(root, p);
  if (!fs.existsSync(f) && fs.existsSync(f + '.html')) f += '.html';
  if (!fs.existsSync(f) || fs.statSync(f).isDirectory()) { r.writeHead(404); return r.end(); }
  r.writeHead(200, { 'content-type': { '.js': 'text/javascript', '.html': 'text/html', '.css': 'text/css' }[path.extname(f)] || 'application/octet-stream' }); fs.createReadStream(f).pipe(r); }).listen(8790);
const b = await chromium.launch({ executablePath: process.env.CHROMIUM || '/opt/pw-browsers/chromium' }); const pg = await b.newPage();
const res = [];
for (const rel of pages) {
  const url = '/' + rel.replace(/\.html$/, '').replace(/(^|\/)index$/, '$1');
  await pg.goto('http://localhost:8790' + url, { waitUntil: 'networkidle' }); await pg.waitForTimeout(800); await pg.waitForFunction(() => window.__rxSpeechText, null, { timeout: 5000 }).catch(() => {});
  const text = await pg.evaluate(() => window.__rxSpeechText ? window.__rxSpeechText() : '');
  const base = await pg.evaluate(() => '/audio' + location.pathname.replace(/\/$/, '/index'));
  if (text.trim()) res.push({ base, text });
}
fs.writeFileSync(out, JSON.stringify(res)); console.log(res.length, 'pages,', res.reduce((a, x) => a + x.text.length, 0), 'characters');
await b.close(); srv.close();
