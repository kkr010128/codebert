import math
import sys

sys.setrecursionlimit(10**9)

MOD = 10**9+7

n, k = map(int, input().split())
k = min(k, n-1)

fact = [1]
for i in range(1, 10**6):
    fact.append((fact[i-1]*i)%MOD)

inv = [None]*10**6
def inv_fact(n):
    if inv[n] == None:
        inv[n] = pow(fact[n], MOD-2, MOD)
    return inv[n]

def comb(n, r):
    return (fact[n]*inv_fact(n-r)*inv_fact(r))%MOD

ans = 0
for i in range(k+1):
    ans = (ans + comb(n-1, i)*comb(n, i))%MOD
print(ans)