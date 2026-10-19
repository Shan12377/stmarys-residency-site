// POST /api/tts {text} -> audio/mpeg. Behind Cloudflare Access with the rest of the site.
// Uses Deepgram Aura-2 on Workers AI (binding "AI" in wrangler.toml, no key).
// If the ELEVENLABS_API_KEY secret is set in Pages settings, uses ElevenLabs instead.
export async function onRequestPost({ request, env }) {
  let text = '';
  try { ({ text } = await request.json()); } catch {}
  if (typeof text !== 'string' || !text.trim() || text.length > 1900)
    return new Response('text must be 1 to 1900 characters', { status: 400 });

  if (env.ELEVENLABS_API_KEY) {
    const voice = env.ELEVENLABS_VOICE_ID || '21m00Tcm4TlvDq8ikWAM';
    const r = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voice}?output_format=mp3_44100_128`, {
      method: 'POST',
      headers: { 'xi-api-key': env.ELEVENLABS_API_KEY, 'content-type': 'application/json' },
      body: JSON.stringify({ text, model_id: env.ELEVENLABS_MODEL || 'eleven_multilingual_v2' }),
    });
    return new Response(r.body, { status: r.status, headers: { 'content-type': r.ok ? 'audio/mpeg' : 'text/plain' } });
  }

  // ponytail: no audio cache; each chunk is generated on play (Aura-2 is $0.03 per 1k characters).
  return env.AI.run('@cf/deepgram/aura-2-en',
    { text, speaker: env.TTS_SPEAKER || 'thalia', encoding: 'mp3' },
    { returnRawResponse: true });
}
