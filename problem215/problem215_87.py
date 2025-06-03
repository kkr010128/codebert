# 逆元を利用した組み合わせの計算
#############################################################
def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod

mod = 10**9 + 7
NN = 10**6

g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range(2, NN + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)
#############################################################

N, K = map(int, input().split())

# M = 空き部屋数の最大値
M = min(N - 1, K)

"""
m = 0,1,2,...,M

N部屋から、空き部屋をm個選ぶ
-> N_C_m

残りの(N-m)部屋に、N人を配置する（空き部屋が出来てはいけない）
まず、(N-m)部屋に1人ずつ配置し、残ったm人を(N-m)部屋に配置する
これは、m個のボールと(N-m-1)本の仕切りの並び替えに相当する
-> (m+N-m-1)_C_m = N-1_C_m
"""

ans = 0
for m in range(0, M + 1):
    ans += cmb(N, m, mod) * cmb(N - 1, m, mod)
    ans %= mod

print(ans)
