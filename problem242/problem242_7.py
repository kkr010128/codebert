def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


p = 10 ** 9 + 7
N = 10 ** 5 + 1  # N は必要分だけ用意する
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)


N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans = 0
for ri in range(2):
    for i in range(N):
        now = cmb(i, K - 1, p)
        if ri == 1:
            now = - now
        ans += A[i] * now
        ans %= p
    A.sort(reverse=True)
print(ans)