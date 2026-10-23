import sys; sys.path.insert(0, sys.path[0])
from qb import write
from m01a import A
from m01b import B
write(sys.argv[1], 'm01', 'Module 1 · Labor & Delivery',
      'Severe blood pressure, magnesium, oxytocin, postpartum hemorrhage, GBS, intraamniotic infection, steroids, tocolysis, Rh, aspirin, induction, diabetes, and pregnancy and breastfeeding safety.', A + B)
