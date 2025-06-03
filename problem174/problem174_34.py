import math
import itertools
def gcd(x,y,z):
    xy = math.gcd(x,y)
    xyz = math.gcd(xy,z)
    return xyz
k1 = int(input())
k = list(range(1,k1+1))
l = []
for i in itertools.combinations_with_replacement(k,3):
    l.append(i)
num = 0
for h in l:
    t = gcd(h[0],h[1],h[2])
    if h[0] == h[1] == h[2]:
        num += t
    elif h[0] == h[1] or h[1] == h[2] or h[2] == h[0]:
        num += 3*t
    else:
        num += 6*t
print(num)    