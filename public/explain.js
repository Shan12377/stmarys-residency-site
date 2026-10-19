// Highlight a word or phrase on any page, tap "Explain", get a short explanation in context.
(() => {
  let btn, card, audio;
  const art = () => document.querySelector('article');

  function context(range) {
    let el = range.commonAncestorContainer;
    if (el.nodeType === 3) el = el.parentElement;
    const block = el.closest('p,li,td,th,blockquote') || el;
    let h = block, heading = '';
    while (h && h !== art()) {
      let s = h.previousElementSibling;
      while (s && !/^H[1-4]$/.test(s.tagName)) s = s.previousElementSibling;
      if (s) { heading = s.innerText; break; }
      h = h.parentElement;
    }
    const row = block.closest('tr');
    const head = row?.closest('table')?.querySelector('tr')?.innerText || '';
    return [heading, head, row ? row.innerText : block.innerText].filter(Boolean).join('\n').slice(0, 2000);
  }

  function hide() { btn?.remove(); btn = null; }
  function close() { card?.remove(); card = null; audio?.pause(); }

  function show() {
    if (card) return; // clicks inside an open card
    const sel = getSelection();
    const term = sel.toString().trim();
    hide();
    if (!term || term.length > 120 || !sel.rangeCount || !art()?.contains(sel.anchorNode)) return;
    const range = sel.getRangeAt(0), r = range.getBoundingClientRect();
    btn = document.createElement('button');
    btn.type = 'button'; btn.textContent = 'Explain';
    btn.style.cssText = `position:absolute;z-index:1000;left:${scrollX + r.left}px;top:${scrollY + r.bottom + 6}px;padding:5px 10px;border-radius:8px;border:1px solid var(--lightgray,#ccc);background:var(--secondary,#1f3b5a);color:#fff;font:600 13px system-ui,sans-serif;cursor:pointer`;
    btn.onmousedown = e => e.preventDefault();
    btn.onclick = () => explain(term, context(range), r);
    document.body.appendChild(btn);
  }

  async function explain(term, ctx, r) {
    hide(); close();
    card = document.createElement('div');
    card.setAttribute('role', 'dialog');
    const top = scrollY + r.bottom + 8, left = Math.max(8, Math.min(scrollX + r.left, scrollX + innerWidth - 376));
    card.style.cssText = `position:absolute;z-index:1001;left:${left}px;top:${top}px;width:min(360px,calc(100vw - 16px));padding:12px 14px;border-radius:12px;background:var(--light,#fff);color:var(--dark,#222);border:1px solid var(--lightgray,#ccc);box-shadow:0 6px 24px rgba(0,0,0,.18);font:14px/1.5 system-ui,sans-serif`;
    card.innerHTML = `<b></b><p style="margin:6px 0 8px">Thinking...</p>
      <div style="display:flex;gap:6px;align-items:center"><button data-a="listen" type="button">▶ Listen</button><button data-a="close" type="button">Close</button></div>
      <small style="display:block;margin-top:8px;opacity:.7">AI explanation. Doses and limits come from the page and its sources.</small>`;
    card.querySelector('b').textContent = term;
    for (const b of card.querySelectorAll('button')) b.style.cssText = 'font:inherit;padding:3px 9px;border-radius:6px;border:1px solid var(--lightgray,#ccc);background:none;color:inherit;cursor:pointer';
    document.body.appendChild(card);
    const p = card.querySelector('p');
    card.querySelector('[data-a=close]').onclick = close;
    try {
      const res = await fetch('/api/explain', { method: 'POST', headers: { 'content-type': 'application/json' },
        body: JSON.stringify({ term, context: ctx, page: document.title }) });
      const { text } = await res.json();
      p.textContent = text || 'No explanation came back. Try a shorter phrase.';
    } catch { p.textContent = 'Could not reach the explainer. Check your connection and try again.'; }
    card.querySelector('[data-a=listen]').onclick = async () => {
      audio?.pause();
      try {
        const res = await fetch('/api/tts', { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ text: p.textContent }) });
        if (!res.ok) throw 0;
        audio = new Audio(URL.createObjectURL(await res.blob())); audio.play();
      } catch { speechSynthesis.speak(new SpeechSynthesisUtterance(p.textContent)); }
    };
  }

  document.addEventListener('mouseup', () => setTimeout(show, 0));
  document.addEventListener('touchend', () => setTimeout(show, 350));
  document.addEventListener('keydown', e => { if (e.key === 'Escape') { hide(); close(); } });
  document.addEventListener('mousedown', e => { if (card && !card.contains(e.target)) close(); });
  document.addEventListener('nav', () => { hide(); close(); });
})();
