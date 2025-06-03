import math
alen, blen, cang = map(float, input().split())
h = math.sin(math.radians(cang)) * blen
#print(h)
S = 0.5 * alen * h
if cang < 90.0:
    L = alen + blen + math.sqrt((alen - math.sqrt(blen**2.0 - h**2.0)) ** 2.0 + h**2.0)
else:
    L = alen + blen + math.sqrt((alen + math.sqrt(blen**2.0 - h**2.0)) ** 2.0 + h**2.0)
print(S)
print(L)
print(h)
