from functools import reduce
from math import gcd, sqrt,ceil


n = int(input())
a = list(map(int,input().split()))
m = 10**6

a_gcd = reduce(gcd,a)
if a_gcd != 1:
    print("not coprime")
    exit(0)
isset = a_gcd == 1
hurui = [i for i in range(m+1)]
for i in range(2,ceil(sqrt(m))+1):
    for j in range(2,ceil(sqrt(i))+1):
        if i==2:
            continue
        if i%j == 0:
            break
    else:
        for k in range(i+i,m,i):
            if hurui[k] != k:
                continue
            hurui[k] = i
    continue
s = set()
p_f = True
for ai in a:
    t = set()
    while(ai > 1):
        t.add(hurui[ai])
        ai //= hurui[ai]
    for ti in t:
        if ti in s:
            print("setwise coprime")
            exit(0)
        else:
            s.add(ti)

print("pairwise coprime")