import sys
X, Y = map(int, input().split())

# たどりつけない時
if ((X+Y) % 3 != 0) or (min(X, Y)*2 < max(X, Y)):
    print(0)
    sys.exit()

# 目的地までの移動回数
n = (X+Y)//3

# 少ない方の使用回数
r = 2*n-max(X, Y)

# n個の中からr個選ぶ組み合わせ
mod = pow(10, 9)+7
bunshi = 1
bunbo = 1
for i in range(r):
    bunshi = (bunshi*(n-i)) % mod
    bunbo = (bunbo*(i+1)) % mod

ans = (bunshi*pow(bunbo, -1, mod)) % mod

print(ans)
