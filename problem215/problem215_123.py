MOD = 1000000007
n,k = map(int,input().split())


fac = [0]*(n+1)
finv = [0]*(n+1)
inv = [0]*(n+1)
answer = 0
# テーブルを作る前処理
def COMinit(n, MOD):
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, n+1):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD
# 二項係数計算
def COM(n, k):
    if (n < k): return 0
    if (n < 0 or k < 0): return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


COMinit(n, MOD)

fac = tuple(fac)
finv = tuple(finv)
inv = tuple(inv)

a = n if n < k else k + 1

for i in range(a):
    answer += COM(n,i) * COM(n-1, n-i-1)
    # print(answer)
print(answer%MOD)
