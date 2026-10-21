"""Make free natural voice audio for each page with Kokoro (open source, runs offline).
Usage: python3 src/make_audio.py speech.json src/audio MODEL_DIR
speech.json comes from src/get_speech_text.mjs. Pages whose text fingerprint is unchanged are skipped.
The Listen button only plays a file when its fingerprint matches the live page, so stale audio is never played."""
import hashlib, json, os, re, subprocess, sys, tempfile, time
import numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
VOICE, SPEED = 'af_heart', 1.0
src, outdir, model = sys.argv[1:4]
order = ['/clinical/', '/drug-hub/monographs/', '/drug-hub/', '/cases/', '/journal-club/', '']
pages = sorted(json.load(open(src)), key=lambda p: next(i for i, o in enumerate(order) if o in p['base']))
k = Kokoro(os.path.join(model, 'kokoro-v1.0.onnx'), os.path.join(model, 'voices-v1.0.bin'))

def pieces(text):
    for para in re.split(r'\n+', text):
        cur = ''
        for s in re.split(r'(?<=[.!?;:])\s+', para.strip()):
            if len(cur) + len(s) > 350 and cur: yield cur, False; cur = ''
            cur = (cur + ' ' + s).strip()
        if cur: yield cur, True   # True = end of paragraph, longer pause

for p in pages:
    h = hashlib.sha256(p['text'].encode('utf-8')).hexdigest()
    base = os.path.join(outdir, p['base'].removeprefix('/audio/'))
    try:
        if json.load(open(base + '.json'))['hash'] == h: continue
    except Exception: pass
    t0 = time.time(); out, sr = [], 24000
    for chunk, endp in pieces(p['text']):
        a, sr = k.create(chunk, voice=VOICE, speed=SPEED, lang='en-us')
        out += [a, np.zeros(int(sr * (0.45 if endp else 0.15)), dtype=a.dtype)]
    os.makedirs(os.path.dirname(base), exist_ok=True)
    with tempfile.NamedTemporaryFile(suffix='.wav') as w:
        sf.write(w.name, np.concatenate(out), sr)
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', w.name, '-ac', '1', '-b:a', '40k', base + '.mp3'], check=True)
    json.dump({'hash': h, 'voice': VOICE, 'made': time.strftime('%Y-%m-%d')}, open(base + '.json', 'w'))
    print(f"{p['base']}: {sum(len(x) for x in out[::2]) / sr / 60:.1f} min audio in {time.time() - t0:.0f}s", flush=True)
print('done', flush=True)
