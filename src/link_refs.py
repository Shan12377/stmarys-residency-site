# Build step: turn [n] citations into links that open source n from the page's "Sources" list.
import re, sys, pathlib
URL = r'\((https?://(?:[^()\s]|\([^()\s]*\))+)\)'
total = 0
for f in pathlib.Path(sys.argv[1]).rglob('*.md'):
    s = f.read_text()
    m = re.search(r'^##+ Sources[^\n]*\n', s, re.M)
    if not m: continue
    body, tail = s[:m.start()], s[m.start():]
    src = {}
    for n, line in re.findall(r'^(\d+)\.\s+(.*)$', tail, re.M):
        u = re.search(URL, line)
        if u and n not in src: src[n] = u.group(1)
    def rep(x):
        global total
        u = src.get(x.group(1))
        if not u: return x.group(0)
        total += 1
        return f'<a href="{u}" target="_blank" rel="noopener" class="ref">[{x.group(1)}]</a>'
    body = re.sub(r'(?<![\w!\]])\[(\d+)\](?![(\[:])', rep, body)
    f.write_text(body + tail)
print(f'linked {total} citations')
