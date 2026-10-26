import json,re,os,sys
Q='/home/claude/stmarys-residency-site/src/qbank'; OUT=sys.argv[1]
D=json.load(open(f'{Q}/drugs.json'))
clean=lambda s: re.sub(r'\*\*|\*','',s or '').strip()
GROUPS=[('01 Foundations and Labor and Delivery',['m00','m01']),
 ('02 Vancomycin, IV Room, IV to PO, Anticoagulation',['m02','m03','m04','m05']),
 ('03 Infectious Disease, Critical Care, Codes, Stroke',['m06','m07','m08','m09']),
 ('04 Trauma, NICU, PICU',['m10','m11','m12']),
 ('05 Med Safety and Florida Law, Practice Advancement, Mixed Patients',['m13','m14','m15'])]
HEAD="""This document is a study source for a hospital staff pharmacist question bank (St. Mary's virtual residency). Every case is an invented teaching case; no patient data.
How to use it: each case lists the questions and all answer choices first, then an Answer and Reasoning section that explains why the correct choice is right and exactly why every other choice is wrong (often because that value belongs to a different situation). Then the full workup: dose math for this patient, what if scenarios, the drug reference cards to review, and sources.
Source marks: ✅✅ two independent sources agree; ✅ one source; ⚠️ verify locally or unverified. St. Mary's order sets and policies override everything here.
"""
L='ABCDEFGH'
def case(c,mt):
    o=[f"## Case {c['id']}: {clean(c['title'])}",f"Module: {mt}. Level: {c.get('level','')}. Setting: {c.get('setting','')}. Topics: {', '.join(c.get('topics',[]))}.",'',f"Scenario: {clean(c['stem'])}"]
    if c.get('chart'): o.append(f"Chart: {clean(json.dumps(c['chart'],ensure_ascii=False) if not isinstance(c['chart'],str) else c['chart'])}")
    for k,s in enumerate(c['steps']):
        o+=['',f"### Question {k+1}: {clean(s['q'])}"+(' (select all that apply)' if s.get('type')=='multi' else '')]
        o+=[f"{L[i]}. {clean(x['t'])}" for i,x in enumerate(s['options'])]
    o+=['','### Answers and reasoning']
    for k,s in enumerate(c['steps']):
        ok=[L[i] for i,x in enumerate(s['options']) if x['correct']]
        o.append(f"Question {k+1} answer: {', '.join(ok)}.")
        for i,x in enumerate(s['options']):
            o.append(f"  {L[i]} ({'correct' if x['correct'] else 'wrong'}): {clean(x['t'])}. {clean(x['why'])}".rstrip())
        for f in ('teach','where'):
            if s.get(f): o.append(f"  {f.title()}: {clean(s[f])}")
    for f,lab in (('pearl','Pearl'),('call','What to say on the call'),('monitor','Monitor'),('alternatives','Alternatives')):
        if c.get(f): o.append(f"{lab}: {clean(c[f])}")
    w=c.get('workup') or {}
    if w.get('calc'): o+=['','### Dose check and math for this patient',clean(w['calc'])]
    if w.get('whatif'):
        o+=['','### What if']
        for x in w['whatif']:
            o.append(f"- {clean(x[0])} Answer: {clean(x[1])}" if isinstance(x,(list,tuple)) else f"- {clean(json.dumps(x,ensure_ascii=False))}")
    if w.get('drugs'): o.append('Drug reference cards to review (see the Drug Reference Cards source): '+'; '.join(D[d]['title'] for d in w['drugs'] if d in D)+'.')
    if c.get('sources'):
        o+=['','Sources:']+[f"- {s['mark']} {clean(s['t'])} {s.get('url','')}".rstrip() for s in c['sources']]
    return '\n'.join(o)
os.makedirs(OUT,exist_ok=True)
for name,ms in GROUPS:
    parts=[f"# St. Mary's Question Bank {name}",HEAD]
    for m in ms:
        d=json.load(open(f'{Q}/{m}.json')); parts+=[f"# Module: {clean(d['title'])}",clean(d.get('intro',''))]
        parts+=[case(c,clean(d['title'])) for c in d['cases']]
    open(f'{OUT}/{name}.md','w').write('\n\n'.join(parts))
parts=["# St. Mary's Question Bank 06 Drug Reference Cards",HEAD]
for k,v in D.items():
    parts.append(f"## {clean(v['title'])}")
    for h,b in v['sections']: parts.append(f"### {clean(h)}\n{clean(b)}")
open(f'{OUT}/06 Drug Reference Cards.md','w').write('\n\n'.join(parts))
