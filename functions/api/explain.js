// POST /api/explain {term, context, page} -> {text}. Behind Cloudflare Access with the rest of the site.
// Explains a highlighted word or phrase using the passage around it. Workers AI, no key.
const SYSTEM = `You are a clinical pharmacy tutor for a hospital staff pharmacist.
Explain the highlighted term as it is used in the passage, in 2 to 4 short plain sentences.
If it is a drug, give its class and why it matters in this passage. If it is an abbreviation, spell it out first.
Never give a dose, rate, level or threshold that is not written in the passage; for numbers, point back to the passage.
If you are not sure, say so. Do not use em dashes. No headings, no lists.`;

const pick = d => d?.output_text
  ?? d?.output?.flatMap(o => o.content || []).find(c => c.type === 'output_text')?.text
  ?? d?.response ?? '';

export async function onRequestPost({ request, env }) {
  let b = {};
  try { b = await request.json(); } catch {}
  const term = String(b.term || '').trim().slice(0, 120);
  const context = String(b.context || '').slice(0, 2000);
  const page = String(b.page || '').slice(0, 120);
  if (!term) return Response.json({ error: 'no term' }, { status: 400 });
  const user = `Page: ${page}\nPassage: ${context}\nHighlighted term: ${term}`;
  let text = '';
  try {
    text = pick(await env.AI.run('@cf/openai/gpt-oss-120b', {
      instructions: SYSTEM, input: user, reasoning: { effort: 'low' },
    }));
  } catch {}
  if (!text) {
    // ponytail: fallback model if gpt-oss is unavailable on this account
    text = pick(await env.AI.run('@cf/meta/llama-3.3-70b-instruct-fp8-fast', {
      messages: [{ role: 'system', content: SYSTEM }, { role: 'user', content: user }], max_tokens: 300,
    }));
  }
  return Response.json({ text: text.replace(/\s*—\s*/g, ', ').trim() });
}
