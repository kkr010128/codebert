k = int(input())
s = input()
l = len(s)
MOD = 10 ** 9 + 7


def comb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


p = MOD
N = 10 ** 6 * 2 + 10 # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

# Sn の位置をx = l-1,l,..,l+k-1まで全て動かす
# pow(25,x-l-1,MOD)* x-1Cl-1 * pow(26,l+k-1-x,MOD) をかければOK
ans = 0
for x in range(l - 1, l + k):
    ans += pow(25, x - l + 1, MOD) * comb(x, l - 1, MOD) * pow(26, l + k - 1 - x, MOD)
    ans %= MOD
print(ans)
"""
# dp[i][j]:k+l の長さの文字列の中で、長さi で、sのj番目の文字列まじで含む文字列の個数とする
# dp[i][j] = dp[i-1][j-1] + dp[i-1][j] * 25 となる
# これだと10**12でTLEなので、まとめる
# 答えたいのは、dp[k+l][l]で初期化はdp[1][1] = 1 dp[1][0] = 25
# l までいったら遷移の仕方が変わって*26を続けるだけで良いようになる
dp = [[0] * (l + 1) for _ in range(k + l + 1)]
dp[0][0] = 1
for i in range(1, k + l + 1):
    for j in range(l + 1):
        if j == l:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] * 26
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] * 25
        dp[i][j] %= MOD
print(dp[k + l][l])
"""
