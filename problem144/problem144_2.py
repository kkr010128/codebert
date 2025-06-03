from decimal import *
from math import *
a, b, h, m = map(float, input().split())
ana = 360*(60*h+m)/720
anb = 360*m/60
an = min(abs(ana-anb), abs(anb-ana))
sint = sin(radians(an))
cost = cos(radians(an))
l = Decimal(((b-a*cost)**2 + (a*sint)**2)**.5)
print(l)