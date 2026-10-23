import sys; sys.path.insert(0, sys.path[0])
from qb import O, S, C, src, write

MUE = src('Afanasjeva J, et al. ASHP guidelines on medication use evaluation. Am J Health Syst Pharm 2021;78:168-175', 'https://doi.org/10.1093/ajhp/zxaa393')
IHI = src('IHI: Model for Improvement', 'https://www.ihi.org/resources/how-to-improve')
QIRES = src('UConn Health HSPP: quality improvement vs research', 'https://ovpr.uchc.edu/services/rics/hspp/resources/quality-assurance-quality-improvement-and-research/')
NICE = src('NICE-SUGAR Study Investigators. N Engl J Med 2009;360:1283-1297', 'https://doi.org/10.1056/NEJMoa0810625')
AMPEXT = src('Agnelli G, et al. AMPLIFY-EXT. N Engl J Med 2013;368:699-708', 'https://doi.org/10.1056/NEJMoa1207541')
BRIDGE = src('Douketis JD, et al. BRIDGE. N Engl J Med 2015;373:823-833', 'https://doi.org/10.1056/NEJMoa1501035')
RENOVE = src('Couturaud F, et al. RENOVE. Lancet 2025;405:725-735', 'https://doi.org/10.1016/S0140-6736(24)02842-3')
LOCAL = {'t': "St. Mary's pharmacy leadership, IRB and P&T processes (verify locally)", 'url': '', 'mark': '⚠️'}

CASES = [
C('pa01', 'Choosing a first project', 'Pharmacy · month 2', ['Projects', 'MUE'],
  'You want one finished project in your first 6 months.',
  [S('What makes a strong first MUE topic?',
     [O('A high alert, high risk, high cost or high volume drug, or one with a new safety alert', True, 'ASHP MUE guideline.'),
      O('Criteria that come straight from a label or guideline, and a small enough patient number to review by hand', True, 'For example magnesium on L&D.'),
      O('Whatever topic is easiest to publish, without asking leadership', False, 'Ask your manager what helps the department.')],
     multi=True, kind='Choose'),
   S('Which kind of fix does the MUE method favor when results miss targets?',
     [O('Hard wired changes: order sets, pump library limits, defaults', True, 'They work even on a busy night.'),
      O('Reminder emails', False, 'Weakest fix.')],
     kind='Fix')],
  pearl='**Pick a high alert drug, guideline criteria, small numbers. Fix with order sets and pump limits.**',
  sources=[MUE, LOCAL]),

C('pa02', 'QI or research?', 'Pharmacy · planning a poster', ['Projects', 'IRB'],
  'Your magnesium MUE is going well and you want to present a poster.',
  [S('Is it QI or research?',
     [O('QI for your own hospital usually is not research, but if you plan to present or publish, ask the IRB for a determination before collecting data', True, 'Research = systematic work for generalizable knowledge with human subjects.'),
      O('Posters never need IRB input', False, 'Ask first.')],
     kind='Classify'),
   S('Where can patient data from the project go?',
     [O('Only inside St. Mary\'s systems, de identified for any presentation', True, ''),
      O('Your personal laptop or email', False, 'Never.')],
     kind='Privacy')],
  pearl='**Planning to present? Ask the IRB before collecting data. Data stays in the hospital.**',
  sources=[QIRES, LOCAL]),

C('pa03', 'PDSA cycles', 'L&D · testing a change', ['Projects', 'QI method'],
  'Your MUE found that urine output was documented on time in only 70% of magnesium patients.',
  [S('What is the IHI Model for Improvement\'s first question?',
     [O('What are we trying to accomplish?', True, 'Then: how will we know a change is an improvement, and what change can we make?'),
      O('Who is to blame?', False, '')],
     kind='Method'),
   S('How do you test a fix?',
     [O('A small Plan Do Study Act cycle: try it on one unit or one shift, measure, adjust', True, ''),
      O('Roll it out hospital wide on day one', False, 'Test small first.')],
     kind='Method')],
  pearl='**Aim, measure, change. Small PDSA cycles.**',
  sources=[IHI]),

C('pa04', 'Reading a trial: absolute risk', 'Journal club · NICE-SUGAR', ['Evidence', 'Statistics'],
  'NICE-SUGAR: 90 day death 27.5% with tight glucose control vs 24.9% with conventional control.',
  [S('Absolute risk increase with tight control?',
     [O('2.6 percentage points (27.5 minus 24.9)', True, ''),
      O('10%', False, 'That is close to the relative increase (2.6 / 24.9).')],
     kind='Math'),
   S('Number needed to harm?',
     [O('About 38 (1 / 0.026)', True, 'Treat about 38 patients with tight control and one extra dies.'),
      O('2.6', False, 'Invert the absolute difference.')],
     kind='Math')],
  pearl='**ARR = difference in rates. NNT or NNH = 1 / ARR.**',
  sources=[NICE]),

C('pa05', 'Reading a trial: NNT', 'Journal club · AMPLIFY-EXT', ['Evidence', 'Statistics'],
  'AMPLIFY-EXT: recurrent VTE 8.8% on placebo vs 1.7% on apixaban 2.5 mg BID over 12 months.',
  [S('Absolute risk reduction and NNT?',
     [O('ARR 7.1 points; NNT about 14 for 12 months', True, '1 / 0.071 = 14.'),
      O('ARR 81%; NNT 1', False, '81% is the relative reduction, not absolute.')],
     kind='Math'),
   S('BRIDGE: major bleeding 3.2% with bridging vs 1.3% without. Number needed to harm from bridging?',
     [O('About 53 (1 / 0.019)', True, 'Bridge about 53 patients and one extra has major bleeding.'),
      O('About 2', False, 'Recheck.')],
     kind='Math')],
  pearl='**Quote absolute numbers to prescribers: "NNT 14," "NNH 53."**',
  sources=[AMPEXT, BRIDGE]),

C('pa06', 'Noninferiority', 'Journal club · RENOVE', ['Evidence', 'Trial design'],
  'RENOVE compared reduced dose and full dose DOACs for extended VTE treatment. Recurrence 2.2% reduced vs 1.8% full; clinically relevant bleeding 9.9% vs 15.2%. Noninferiority was not met.',
  [S('What does "noninferiority not met" mean?',
     [O('The trial could not prove reduced dose is not meaningfully worse at preventing recurrence; it does not prove it is worse either', True, ''),
      O('Reduced dose is proven dangerous', False, 'Not what the result says.')],
     kind='Interpret'),
   S('How do you use this at the bedside?',
     [O('Weigh lower bleeding against uncertain recurrence protection for each patient, alongside CHEST 2021 guidance', True, ''),
      O('Ignore it', False, '')],
     kind='Apply')],
  pearl='**Noninferiority not met = not proven as good, not proven worse. Weigh benefits and harms.**',
  sources=[RENOVE]),

C('pa07', 'Documenting your value', 'Pharmacy · monthly review', ['Professional', 'Interventions'],
  'Your manager asks what you contributed this month.',
  [S('What do you track?',
     [O('Interventions by category (renal dose, allergy clarified, IV to PO, duplicates, errors caught), with no patient identifiers in your own notes', True, 'Use the official system for patient level documentation.'),
      O('Nothing; it is all in your head', False, 'Undocumented work is invisible.')],
     kind='Track')],
  pearl='**Count what you catch. Numbers show your value.**',
  sources=[LOCAL]),

C('pa08', 'Giving an inservice', 'L&D · 15 minute nursing inservice', ['Professional', 'Teaching'],
  'You will teach L&D nurses about magnesium toxicity.',
  [S('Which outline works best for 15 minutes?',
     [O('Why it matters (high alert), what the nurse sees first (reflexes before breathing), the numbers, the antidote, one case, 3 questions', True, 'Short, practical, case based.'),
      O('Forty slides of pharmacokinetics', False, 'Too long for the audience and time.')],
     kind='Teach')],
  pearl='**Inservice: why, what you see, numbers, antidote, one case, three questions.**',
  sources=[LOCAL]),
]

if __name__ == '__main__':
    write(sys.argv[1], 'm14', 'Module 14 · Practice Advancement',
          'Choosing an MUE, QI vs research and the IRB, PDSA cycles, reading trials (ARR, NNT, NNH, noninferiority) with real trial numbers, documenting interventions and teaching an inservice.', CASES)
