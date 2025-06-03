from collections import deque,defaultdict
import bisect
N = int(input())
S = [input() for i in range(N)]

def bend(s):
    res = 0
    k = 0
    for th in s:
        if th == '(':
            k += 1
        else:
            k -= 1
        res = min(k,res)
    return res

species = [(bend(s),s.count('(')-s.count(')')) for s in S]

ups = [(b,u) for b,u in species if u > 0]
flats = [(b,u) for b,u in species if u == 0]
downs = [(b,u) for b,u in species if u < 0]


ups.sort()
high = 0
for b,u in ups[::-1] + flats:
    if high + b < 0:
        print('No')
        exit()
    high += u

rdowns = [(b-u,-u) for b,u in downs]
rdowns.sort()
high2 = 0
for b,u in rdowns[::-1]:
    if high2 + b < 0:
        print('No')
        exit()
    high2 += u

if high == high2:
    print('Yes')
else:
    print('No')
