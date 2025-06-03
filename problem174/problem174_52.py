import math
import itertools

k = int(input())
l = list(range(1,k+1))
y = list(itertools.combinations_with_replacement(l,3))
n = len(y)
t = 0

for i in range(n):
    a = y[i][0]
    b = y[i][1]
    c = y[i][2]
    d = math.gcd(math.gcd(a,b),c)
    if a != b != c:
        t += d * 6
    elif a == b == c:
        t += d
    else:
        t += d * 3

print(t)