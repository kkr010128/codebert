N, M, K = map(int, input().split())
MOD = 998244353

# 階乗 & 逆元計算
factorial = [1]
inverse = [1]
for i in range(1, N+2):
    factorial.append(factorial[-1] * i % MOD)
    inverse.append(pow(factorial[-1], MOD - 2, MOD))

# 組み合わせ計算
def nCr(n, r):
    if n < r or r < 0:
        return 0
    elif r == 0:
        return 1
    return factorial[n] * inverse[r] * inverse[n - r] % MOD

ans = 0
for k in range(K + 1):
    ans += M * nCr(N - 1, k) * pow(M - 1, N - 1 - k, MOD) % MOD
    ans %= MOD

print(ans % MOD)
