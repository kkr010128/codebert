#####################################################
# 組み合わせを10**9+7で割った余り、を高速に求めるアルゴリズム
# https://drken1215.hatenablog.com/entry/2018/06/08/210000
# https://qiita.com/derodero24/items/91b6468e66923a87f39f
# 全然理解できていない
MOD = 10**9 + 7


def comb(n, r):
    if (r < 0 and r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % MOD

N = 10**6
# 元テーブル
g1 = [1, 1]
# 逆元テーブル
g2 = [1, 1]
# 逆元テーブル計算用テーブル
inverse = [0, 1]

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % MOD)
    inverse.append((-inverse[MOD % i] * (MOD // i)) % MOD)
    g2.append((g2[-1] * inverse[-1]) % MOD)


#####################################################

X, Y = map(int, input().split())

# X+Yが3の倍数のマスしか通りえない
if not (X + Y) % 3:

    # (1,2)移動をn回、(2,1)移動をm回したとする
    # n+2m = X, 2n+m = Y
    # → n+m = (X+Y)/3
    # n = (2n+m)-(n+m) = X - (X+Y)/3 = (-X+2Y)/3
    # mも同様
    n = (2 * Y - X) // 3
    m = (2 * X - Y) // 3

    if n >= 0 and m >= 0:
        print(comb(n + m, n))
    else:
        print(0)

# X+Yが3の倍数でない場合
else:
    print(0)
