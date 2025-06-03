MAX = 600000
MOD = 10 ** 9 + 7
fac = [0] * MAX
ifac = [0] * MAX
fac[0] = 1
for i in range(1,MAX):
    fac[i] = (fac[i-1] * i) % MOD
ifac[MAX-1] = pow(fac[MAX-1],MOD-2,MOD)
for i in reversed(range(1,MAX)):
    ifac[i-1] = (ifac[i] * i) % MOD

def combinations(n, k):
    if k < 0 or n < k:
        return 0
    else:
        return (fac[n] * ifac[k] * ifac[n-k]) % MOD

ans = 0
S = int(input())
for i in range(1,1000):
    ans += combinations((S+i-1)-i*3,i-1)
    ans %= MOD
print(ans)

