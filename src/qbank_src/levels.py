# Difficulty per case. F = Foundation (never miss on day one), T = Top 10% (the catch that earns trust). Anything not listed = Staff (solid alone on nights).
F = set('''h01 h02 h03 h04 h05 h06 h07 h08 h09 h10 h11 h12 h13 h14
ld01 ld05 ld07 ld15 ld21 ld22 ld27 ld30 ld31 ld35
pk01 pk02 pk03 pk07 pk12 pk13
iv01 iv02 iv04 iv07 iv11
po01 po02
ac01 ac02 ac10 ac12
id01 id03 id08 id09
cc01 cc09
cd01 cd02 cd10
st01 st02
tr01 tr07
nc01 nc02 nc04
pi01 pi08
ms01 ms03 ms08
pa07 pa08'''.split())
T = set('''ld11 ld13 ld16 ld18 ld20 ld24 ld28 ld33 ld37 ld40
pk04 pk05 pk06 pk08 pk09 pk10 pk17
iv03 iv05 iv09 iv10 iv13
po04 po06 po07
ac05 ac06 ac11 ac13 ac16
id02 id06 id11 id12
cc04 cc06 cc08
cd06 cd11 cd12
st04 st05 st08
tr02 tr05 tr09
nc06 nc07 nc10
pi05 pi07
ms07
pa04 pa05 pa06'''.split())
def level(cid): return 'Top 10%' if cid in T or cid.startswith('mx') else 'Foundation' if cid in F else 'Staff'
