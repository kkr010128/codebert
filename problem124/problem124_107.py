k = int(input())
S = input()
n = len(S)
mod = 10**9+7

facs = [1] * (n+k)
# invs = [1] * (n+k)
nfac = 1
for i in range(1, n+k):
    nfac = nfac * i % mod
    facs[i] = nfac
    # invs[i] = pow(facs[i], mod-2, mod)
invn1 = pow(facs[n-1], mod-2, mod)

ans = 0
for i in range(k+1):
    left = facs[i+n-1] * pow(facs[i], mod-2, mod) * invn1 % mod
    left = left * pow(25, i, mod) % mod
    ans += left * pow(26, k-i, mod) % mod
    ans %= mod
print(ans)
