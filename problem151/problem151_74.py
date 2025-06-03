# E - Colorful Blocks
import sys
readline = sys.stdin.readline

MOD = 998244353
N, M, K = map(int, readline().split())

# 予め階乗を計算しておく
f = [1]
for i in range(N):
    f.append(f[i] * (i+1) % MOD)

f_inv = [1] * N
f_inv[N-1] = pow(f[N-1], MOD-2, MOD)
for i in range(N-1)[::-1]:
    f_inv[i] = f_inv[i+1] * (i+1) % MOD

# 組み合わせ関数
def comb_mod(n, r, p):
    return (f[n] * f_inv[r] * f_inv[n-r])%p

ans = 0
for i in range(K+1):
    ans = (ans + (M*pow(M-1, N-1-i, MOD)) * comb_mod(N-1, i, MOD))%MOD

print(ans)
