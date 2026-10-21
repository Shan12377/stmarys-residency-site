// Read aloud bar for every wiki page. Order: 1) free pre-made audio in /audio (Kokoro, made by src/make_audio.py)
// when its text fingerprint matches the page, 2) /api/tts (free daily allowance), 3) the browser's own voice.
(() => {
  const SILENT = 'data:audio/wav;base64,UklGRrQBAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YZABAACAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA';
  let audio = null, chunks = [], i = 0, next = null, rate = 1, playing = false, run = 0;

  const clean = t => t
    .replace(/✅✅/g, ' two sources. ').replace(/✅/g, ' one source. ').replace(/⚠️/g, ' verify. ')
    .replace(/\[(\d+)\]/g, '').replace(/[·❯]/g, ', ').replace(/\s*\|\s*/g, ', ')
    .replace(/\t+/g, ', ').replace(/[  ]+/g, ' ');

  // Say units and abbreviations the way a pharmacist would read them aloud.
  const UNITS = [['mcg/kg/min','micrograms per kilogram per minute'],['mg/kg/day','milligrams per kilogram per day'],['mg/kg/h','milligrams per kilogram per hour'],
    ['units/kg/h','units per kilogram per hour'],['mg/kg','milligrams per kilogram'],['units/kg','units per kilogram'],['mL/kg','milliliters per kilogram'],
    ['units/h','units per hour'],['mEq/L','milliequivalents per liter'],['mEq/h','milliequivalents per hour'],['mmol/L','millimoles per liter'],['mg/dL','milligrams per deciliter'],
    ['mcg/mL','micrograms per milliliter'],['mg/mL','milligrams per milliliter'],['mL/h','milliliters per hour'],['mL/min','milliliters per minute'],['mg/min','milligrams per minute'],
    ['mcg/min','micrograms per minute'],['g/h','grams per hour'],['mEq','milliequivalents'],['mcg','micrograms'],['mg','milligrams'],['mL','milliliters'],['kg','kilograms'],['g','grams'],['h','hours'],['min','minutes']];
  const ABBR = [[/\bBID\b/g,'twice daily'],[/\bTID\b/g,'three times daily'],[/\bQID\b/g,'four times daily'],[/\bq(\d+)h\b/g,'every $1 hours'],[/\bq(\d+) to (\d+)h\b/g,'every $1 to $2 hours'],
    [/\bPRN\b/g,'as needed'],[/\bPO\b/g,'by mouth'],[/\bSC\b/g,'subcutaneous'],[/\bIM\b/g,'I M'],[/\bx (\d)/g,'for $1'],[/\b(\d{2,3})\/(\d{2,3})\b/g,'$1 over $2']];
  const say = t => {
    for (const [r, w] of ABBR) t = t.replace(r, w);
    for (const [u, w] of UNITS) t = t.replace(new RegExp('(\\d)\\s*' + u.replace(/\//g, '\\/') + '(?![A-Za-z/])', 'g'), '$1 ' + w);
    return t.replace(/(^|[^\d.])1 (gram|milligram|microgram|milliliter|kilogram|hour|minute|milliequivalent)s\b/g, '$11 $2');
  };

  // The exact text that is read aloud for this page (the audio generator calls this too).
  function pageText() {
    const art = document.querySelector('article');
    if (!art) return '';
    // Leave out diagrams and code blocks (they render late and read badly), then restore them.
    const hide = [...art.querySelectorAll('.mermaid, pre, svg, figure, img, script, style')];
    const was = hide.map(e => e.style.display); hide.forEach(e => { e.style.display = 'none'; });
    const raw = art.innerText;
    hide.forEach((e, n) => { e.style.display = was[n]; });
    // Skip the button label and the link list at the bottom ("Sources" heading onward).
    return say(clean(raw.replace(/^\s*\S*\s*(Listen to this page|Pause reading|Resume reading)\s*/, '').split(/\n\s*Sources[^\n:]*\n/)[0]));
  }
  window.__rxSpeechText = pageText;

  async function sha(t) {
    const b = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t));
    return [...new Uint8Array(b)].map(x => x.toString(16).padStart(2, '0')).join('');
  }

  // 1) Pre-made audio, only if it was made from exactly this text.
  async function premade(text, id) {
    try {
      const base = '/audio' + location.pathname.replace(/\/$/, '/index');
      const meta = await fetch(base + '.json', { cache: 'no-cache' }).then(r => r.ok ? r.json() : null);
      if (!meta || id !== run || meta.hash !== await sha(text)) return false;
      audio.src = base + '.mp3?v=' + meta.hash.slice(0, 8); audio.playbackRate = rate;
      audio.onended = stop;
      await audio.play();
      label('Pause', 'Natural voice');
      return true;
    } catch { return false; }
  }

  function split(text) {
    const out = []; let cur = '';
    for (const s of text.split(/(?<=[.!?:;])\s+|\n+/)) {
      if (!s.trim()) continue;
      if ((cur + ' ' + s).length > 1500 && cur) { out.push(cur); cur = ''; }
      cur = cur ? cur + ' ' + s : s;
      while (cur.length > 1500) { out.push(cur.slice(0, 1500)); cur = cur.slice(1500); }
    }
    if (cur.trim()) out.push(cur);
    return out;
  }

  const fetchChunk = n => n < chunks.length
    ? fetch('/api/tts', { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ text: chunks[n] }) })
        .then(r => r.ok ? r.blob() : Promise.reject(r.status))
    : Promise.resolve(null);

  // Browser voice fallback: Chrome goes silent on very long utterances, so speak one sentence at a time.
  function browserVoice(from, why) {
    const parts = chunks.slice(from).join(' ').split(/(?<=[.!?;:])\s+/).flatMap(p => p.match(/.{1,220}(\s|$)/g) || []);
    const id = run; let k = 0;
    const pickVoice = () => {
      const vs = speechSynthesis.getVoices().filter(v => v.lang.startsWith('en'));
      return vs.find(v => /premium|enhanced|natural|google us|samantha|ava|allison/i.test(v.name)) || vs[0] || null;
    };
    const say = () => {
      if (id !== run) return;
      if (k >= parts.length) return stop();
      const u = new SpeechSynthesisUtterance(parts[k++]);
      u.voice = pickVoice(); u.rate = rate; u.onend = say; u.onerror = say;
      speechSynthesis.speak(u);
    };
    speechSynthesis.cancel(); label('Pause', why || 'Browser voice'); say();
  }

  async function play(n, id) {
    if (id !== run) return;
    if (n >= chunks.length) return stop();
    i = n; label('Pause', `Part ${n + 1} of ${chunks.length}`);
    let blob;
    try { blob = await (next || fetchChunk(n)); } catch (e) { return id === run && browserVoice(n, e === 429 ? 'Browser voice (natural voice limit reached today)' : 'Browser voice'); }
    if (id !== run) return;
    next = fetchChunk(n + 1); next.catch(() => {});
    audio.src = URL.createObjectURL(blob); audio.playbackRate = rate;
    audio.onended = () => { URL.revokeObjectURL(audio.src); play(n + 1, id); };
    audio.play().catch(() => id === run && browserVoice(n));
  }

  function toggle() {
    if (playing) {
      playing = false; audio.pause(); speechSynthesis.pause(); return label('Resume');
    }
    playing = true;
    if (audio.src && !audio.ended && audio.currentTime) { audio.play(); return label('Pause'); }
    if (speechSynthesis.paused) { speechSynthesis.resume(); return label('Pause'); }
    const text = pageText();
    if (!text) return;
    // Unlock audio inside the tap so phones allow playback after the voice loads.
    audio.src = SILENT; audio.play().catch(() => {});
    label('Pause', 'Loading voice...');
    chunks = split(text); next = null; const id = ++run;
    premade(text, id).then(ok => { if (!ok && id === run) play(0, id); });
  }

  function stop() {
    run++; playing = false; next = null;
    if (audio) { audio.pause(); audio.removeAttribute('src'); }
    speechSynthesis.cancel(); label('Listen', '');
  }

  function label(btn, status) {
    const b = document.getElementById('rx-listen-btn'), s = document.getElementById('rx-listen-status'), t = document.getElementById('rx-listen-top');
    if (b) b.textContent = btn === 'Listen' ? '▶ Listen' : btn === 'Pause' ? '❚❚ Pause' : '▶ Resume';
    if (t) t.textContent = btn === 'Listen' ? '🔊 Listen to this page' : btn === 'Pause' ? '❚❚ Pause reading' : '▶ Resume reading';
    if (s && status !== undefined) s.textContent = status;
  }

  function mountTop() {
    const art = document.querySelector('article');
    if (!art || document.getElementById('rx-listen-top')) return;
    const t = document.createElement('button');
    t.id = 'rx-listen-top'; t.type = 'button'; t.textContent = '🔊 Listen to this page';
    t.style.cssText = 'display:inline-block;margin:0 0 14px;padding:9px 16px;border-radius:999px;border:0;background:var(--secondary,#1f3b5a);color:#fff;font:600 15px system-ui,sans-serif;cursor:pointer';
    t.onclick = toggle;
    art.prepend(t);
  }

  function mount() {
    mountTop();
    if (document.getElementById('rx-listen') || !document.querySelector('article')) return;
    audio = audio || new Audio();
    const bar = document.createElement('div');
    bar.id = 'rx-listen';
    bar.innerHTML = `<button id="rx-listen-btn" type="button">▶ Listen</button>
      <button id="rx-listen-stop" type="button" aria-label="Stop">■</button>
      <select id="rx-listen-rate" aria-label="Speed"><option>0.9</option><option selected>1</option><option>1.15</option><option>1.3</option><option>1.5</option></select>
      <span id="rx-listen-status" aria-live="polite"></span>`;
    bar.style.cssText = 'position:fixed;right:16px;bottom:16px;z-index:999;display:flex;gap:6px;align-items:center;padding:8px 10px;border-radius:10px;background:var(--light,#fff);border:1px solid var(--lightgray,#ccc);box-shadow:0 2px 10px rgba(0,0,0,.15);font:14px system-ui,sans-serif;color:var(--dark,#222)';
    for (const el of bar.querySelectorAll('button,select')) el.style.cssText = 'font:inherit;padding:4px 8px;border-radius:6px;border:1px solid var(--lightgray,#ccc);background:var(--light,#fff);color:inherit;cursor:pointer';
    document.body.appendChild(bar);
    bar.querySelector('#rx-listen-btn').onclick = toggle;
    bar.querySelector('#rx-listen-stop').onclick = stop;
    bar.querySelector('#rx-listen-rate').onchange = e => { rate = +e.target.value; if (audio) audio.playbackRate = rate; };
    rate = 1;
  }

  document.addEventListener('nav', () => { stop(); mount(); });
  if (document.readyState !== 'loading') mount(); else document.addEventListener('DOMContentLoaded', mount);
})();
