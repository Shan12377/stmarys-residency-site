# Small helpers so case files read like plain writing. Output: JSON the question bank loads.
import json, os

def O(t, ok=False, why=''):
    return {'t': t, 'correct': ok, 'why': why}

def S(q, opts, teach='', where='', kind='', multi=False, seconds=None):
    d = {'q': q, 'options': opts, 'teach': teach, 'where': where, 'kind': kind}
    if multi: d['type'] = 'multi'
    if seconds: d['seconds'] = seconds
    assert any(o['correct'] for o in opts), q
    return d

def C(id, title, setting, topics, stem, steps, chart=None, call='', monitor='', pearl='', alternatives='', sources=()):
    return {'id': id, 'title': title, 'setting': setting, 'topics': topics, 'stem': stem, 'chart': chart,
            'steps': steps, 'call': call, 'monitor': monitor, 'pearl': pearl, 'alternatives': alternatives,
            'sources': list(sources)}

def src(t, url, mark='✅'):
    return {'t': t, 'url': url, 'mark': mark}

def write(outdir, mid, title, intro, cases):
    from levels import level
    from workups import W
    from drugcards import write_cards, CARDS
    for c in cases:
        c['level'] = level(c['id'])
        if c['id'] in W:
            assert all(d in CARDS for d in W[c['id']]['drugs']), c['id']
            c['workup'] = W[c['id']]
    write_cards(outdir)
    ids = [c['id'] for c in cases]; assert len(ids) == len(set(ids)), 'duplicate case id'
    os.makedirs(outdir, exist_ok=True)
    json.dump({'id': mid, 'title': title, 'intro': intro, 'cases': cases}, open(f'{outdir}/{mid}.json', 'w'), ensure_ascii=False, indent=1)
    idx_path = f'{outdir}/index.json'
    idx = json.load(open(idx_path)) if os.path.exists(idx_path) else []
    idx = [m for m in idx if m['id'] != mid] + [{'id': mid, 'title': title, 'count': len(cases)}]
    idx.sort(key=lambda m: m['id'])
    json.dump(idx, open(idx_path, 'w'), ensure_ascii=False, indent=1)
    print(mid, len(cases), 'cases,', sum(len(c['steps']) for c in cases), 'steps')
