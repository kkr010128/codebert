MOD = 10 ** 9 + 7
MAX = 10 ** 6 + 1
fac = [0] * MAX
finv = [0] * MAX
inv = [0] * MAX

def CoMinit():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

def COM(n, k):
   if n < k:
       return 0
   if n < 0 or k < 0:
       return 0

   return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD
CoMinit()

N, K = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

mint = 0
maxt = 0
for i in range(N):
    maxt += a[i] * COM(i, K - 1)
    mint += a[-i - 1] * COM(i, K - 1)

print((maxt - mint) % MOD)