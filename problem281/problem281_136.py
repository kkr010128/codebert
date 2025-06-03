# https://atcoder.jp/contests/abc145/tasks/abc145_d

X, Y = list(map(int, input().split()))
MOD = int(1e9 + 7)

def combination(n, r, mod=MOD):
    def modinv(a, mod=MOD):
        return pow(a, mod-2, mod)
    # nCr with MOD
    r = min(r, n - r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res

# 1回の移動で3増えるので，X+Yは3の倍数 (0, 0) start
if (X + Y) % 3 != 0:
    ans = 0
    print(0)
else:
    # X+Yは3の倍数
    # (+1, +2)をn回，(+2, +1)をm回実行
    # n + 2m = X
    # 2n + m = Y
    # 3 m = 2 X - Y
    # m = (2 X - Y) // 3
    # n = X - 2 * m
    
    m = (2 * X - Y) // 3
    n = X - 2 * m

    if m < 0 or n < 0:
        print(0)
    else:
        print(combination(m + n, m, MOD))
