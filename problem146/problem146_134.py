import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import defaultdict

MOD = 10**9+7
N = int(input())
dic = defaultdict(int)
zero = 0
left_zero = 0
right_zero = 0
for i in range(N):
    a, b = map(int, input().split())
    if b < 0:
        a = -a
        b = -b
    if a == 0 and b == 0:
        zero += 1
    elif a == 0:
        left_zero += 1
    elif b == 0:
        right_zero += 1
    else:
        g = math.gcd(a, b)
        a //= g
        b //= g
        dic[a,b] += 1
done = set()
ans = 1
for a,b in dic:
    k = (a, b)
    if k in done: continue
    rk = (-b, a)
    rk2 = (b, -a)
    done.add(k)
    done.add(rk)
    done.add(rk2)
    c = pow(2, dic[k], MOD)-1
    if rk in dic:
        c += pow(2, dic[rk], MOD)-1
    if rk2 in dic:
        c += pow(2, dic[rk2], MOD)-1
    c += 1
    ans *= c
    ans %= MOD
c1 = pow(2, left_zero, MOD)-1
c2 = pow(2, right_zero, MOD)-1
c = c1+c2+1
ans *= c
ans += zero
print((ans-1)%MOD)
