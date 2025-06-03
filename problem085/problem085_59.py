import sys
from math import gcd

n = int(input())
a = list(map(int, input().split()))

b = gcd(a[0], a[1])
for i in range(2, n):
    b = gcd(b, a[i])
if b != 1:
    print('not coprime')
else:
    c = set()
    num = max(a)
    m = 1000000
    vals = [0]*(m+1)

    for i in range(2, m):
        if vals[i] != 0:
            continue
        j = 1
        while True:
            t = i*j
            if t > m:
                break
            if vals[t] == 0:
                vals[t] = i
            j += 1
    d = dict()
    for i in a:
        p = i
        while p != 1:
            if p in d:
                print("setwise coprime")
                sys.exit()
            d[p] = 1
            p = int(p/vals[p])
    print("pairwise coprime")
