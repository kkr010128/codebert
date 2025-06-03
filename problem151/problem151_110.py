def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 998244353
N = 2 * 10**5  # 出力の制限
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)


N, M, K = map(int, input().split())

m_pow = [0] * N
m_pow[0] = 1

for i in range(1, N):
    m_pow[i] = m_pow[i - 1] * (M - 1) % mod

ans = 0

for i in range(K+1):
    ans = (ans + cmb(N - 1, i, mod) * M * m_pow[N - 1 - i]) % mod

print(ans)
