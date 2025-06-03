# 二項係数のmod (大量のmod計算が必要なとき)
def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r=min(r,n-r)

    return g1[n] * g2[r] * g2[n - r] % mod

mod=998244353
N = 10 ** 6 # 出力の制限
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

n,m,k= map(int, input().split())


ans=0

# 同じ色で塗る組数で場合分け
for i in range(k,-1,-1):
    # 同色の組の色の割り当て
    if i==k:
        v1 = m * pow(m - 1, n - i - 1, mod)
    else:
        v1*=m-1
        v1%=mod
    # グループの分け方
    v2=cmb(n-1,i,mod)
    ans+=v1*v2
    ans%=mod

print(ans)