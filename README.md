# St. Mary's Virtual Residency (private)

- `src/` is the source: wiki pages, index, log, What's New (`src/whats_new.md`), and tool pages. Edit here.
- `bash build.sh` builds the site into `public/`.
- Cloudflare Pages serves `public/` from `main` (build command none, output `public`), behind Cloudflare Access.
- Rules: see `src/CLAUDE.md`. No patient information, no names of colleagues, no St. Mary's internal documents, no copied commercial reference content.
- Monthly update: a scheduled task opens a pull request with source checks and a new What's New entry. Merge it to publish.
- Read aloud: `src/listen.js` adds a Listen bar to every page; `functions/api/tts.js` makes the audio with Deepgram Aura-2 on Workers AI (binding in `wrangler.toml`). Set the secret `ELEVENLABS_API_KEY` (optional `ELEVENLABS_VOICE_ID`) in Pages settings to switch to ElevenLabs.
- Explain: `src/explain.js` shows an Explain button on highlighted text; `functions/api/explain.js` answers with gpt-oss-120b on Workers AI (falls back to Llama 3.3 70B). It is told never to add doses that are not on the page.
- Citations: `src/link_refs.py` runs during the build and turns each [n] into a link to source n in that page's Sources list. Write sources as `n. [Title](url)`.
- Free voice: `src/audio/` holds Kokoro audio per page plus a fingerprint file. Remake with: `node src/get_speech_text.mjs public speech.json` then `python3 src/make_audio.py speech.json src/audio <kokoro model folder>` (needs Playwright, kokoro-onnx, ffmpeg). The Listen button plays a file only when its fingerprint matches the live page.
