X,Y = map(int,input().split())

MAX_NUM = 10**6 + 1
MOD = 10**9+7

fac  = [0 for _ in range(MAX_NUM)]
finv = [0 for _ in range(MAX_NUM)]
inv  = [0 for _ in range(MAX_NUM)]

fac[0]  = fac[1] = 1
finv[0] = finv[1] = 1
inv[1] = 1

for i in range(2,MAX_NUM):
    fac[i] = fac[i-1] * i % MOD
    inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
    finv[i] = finv[i-1] * inv[i] % MOD

def combinations(n,k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n-k] % MOD) % MOD

if (X+Y)%3 != 0:
    answer = 0
else:
    up = -(X+Y)//3+Y
    right = -(X+Y)//3+X
    answer = combinations(up+right,up)
print(answer)