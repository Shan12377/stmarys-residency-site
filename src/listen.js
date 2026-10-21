// Read aloud bar for every wiki page. Audio comes from /api/tts (Aura-2 or ElevenLabs).
// Falls back to the browser's own voice if the server voice fails.
(() => {
  const SILENT = 'data:audio/wav;base64,UklGRrQBAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YZABAACAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA';
  let audio = null, chunks = [], i = 0, next = null, rate = 1, playing = false, run = 0;

  const clean = t => t
    .replace(/✅✅/g, ' two sources. ').replace(/✅/g, ' one source. ').replace(/⚠️/g, ' verify. ')
    .replace(/\[(\d+)\]/g, '').replace(/[·❯]/g, ', ').replace(/\s*\|\s*/g, ', ')
    .replace(/\t+/g, ', ').replace(/[  ]+/g, ' ');

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
    const art = document.querySelector('article');
    if (!art) return;
    // Unlock audio inside the tap so phones allow playback after the voice loads.
    audio.src = SILENT; audio.play().catch(() => {});
    label('Pause', 'Loading voice...');
    // Skip the link list at the bottom ("Sources" heading onward).
    chunks = split(clean(art.innerText.replace(/^\s*\S*\s*(Listen to this page|Pause reading|Resume reading)\s*/, '').split(/\n\s*Sources[^\n:]*\n/)[0])); next = null; run++;
    play(0, run);
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
