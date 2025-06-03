N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

ans = 0
for i in range(N - K + 1):
    ans -= A[i] * cmb(N - 1 - i, K - 1, p)
A = A[::-1]
for i in range(N - K + 1):
    ans += A[i] * cmb(N - 1 - i, K - 1, p)
print(ans % p)