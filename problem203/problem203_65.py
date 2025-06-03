from math import floor
from math import ceil
a,b = map(int,input().split())
n = floor(a / 0.08)
m = floor(b / 0.1)
n2 = ceil(a / 0.08)
m2 = ceil(b / 0.1)
p = floor(n * 0.08)
q = floor(n * 0.1)
p2 = floor(n2 * 0.08)
q2 = floor(n2 * 0.1)
x = floor(m * 0.08)
y = floor(m * 0.1)
x2 = floor(m2 * 0.08)
y2 = floor(m2 * 0.1)
if p == a and q == b and x == a and y == b:
    print(min(n,m))
elif p == a and q == b:
    print(n)
elif x == a and y == b:
    print(m)
elif p2 == a and q2 == b and x2 == a and y2 == b:
    print(min(n2,m2))
elif p2 == a and q2 == b:
    print(n2)
elif x2 == a and y2 == b:
    print(m2)
else:
    print(-1)