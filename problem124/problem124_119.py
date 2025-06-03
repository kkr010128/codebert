import sys
readline = sys.stdin.readline
MOD = 10**9+7
def frac(limit):
    frac = [1]*limit
    for i in range(2,limit):
        frac[i] = i * frac[i-1]%MOD
    fraci = [None]*limit
    fraci[-1] = pow(frac[-1], MOD -2, MOD)
    for i in range(-2, -limit-1, -1):
        fraci[i] = fraci[i+1] * (limit + i + 1) % MOD
    return frac, fraci

frac, fraci = frac(2341398)
def cmb(a, b):
    if not a >= b >= 0:
        return 0
    return frac[a]*fraci[b]*fraci[a-b]%MOD

K, = map(int, input().split())
t = len(input().strip())

R = 0
for x in range(K+1):
    R += cmb(K+t-x-1, t-1)*pow(25, K-x, MOD)*pow(26, x, MOD)%MOD
    R %= MOD
print(R)
