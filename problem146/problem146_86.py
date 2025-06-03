import sys
from math import gcd
from collections import defaultdict


def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())


N = I()
mod = 10**9+7
plus = defaultdict(int)
minus = defaultdict(int)
flag = defaultdict(int)
A_zero,B_zero = 0,0
zero_zero = 0
for i in range(N):
    a,b = MI()
    if a == b == 0:
        zero_zero += 1
    elif a == 0:
        A_zero += 1
    elif b == 0:
        B_zero += 1
    else:
        if a < 0:
            a,b = -a,-b
        a,b = a//gcd(a,b),b//gcd(a,b)
        if b > 0:
            plus[(a,b)] += 1
        else:
            minus[(a,b)] += 1
            flag[(a,b)] = 0

ans = 1

for a,b in plus.keys():
    ans *= pow(2,plus[(a,b)],mod)+pow(2,minus[(b,-a)],mod)-1
    ans %= mod
    flag[(b,-a)] = 1

for key in minus.keys():
    if flag[key] == 0:
        ans *= pow(2,minus[key],mod)
        ans %= mod

ans *= pow(2,A_zero,mod)+pow(2,B_zero,mod)-1
ans %= mod

ans += zero_zero-1
ans %= mod

print(ans)
