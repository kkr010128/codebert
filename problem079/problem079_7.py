import sys 
 
S = int(sys.stdin.readline())
mod = 10**9 + 7
 
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
 
for i in range(2, 2*S+1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)
 
def nCr(n, r, mod=10**9+7):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % mod
 
ans = 0
n = 1
n_max = S // 3
while n <= n_max:
    res = S - 3 * n
    tmp = nCr(res + n - 1, n - 1)
    # print(n, res, tmp)
    ans += tmp
    ans %= mod
    n += 1
 
print(ans)