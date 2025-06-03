H, W = map(int, input().split())
L = [input() for _ in range(H)]
 
inf = 10**9
dp = [[inf] * W for _ in range(H)]
 
#[0][0]を埋める
if (L[0][0] == '.'):
    dp[0][0] = 0
else:
    dp[0][0] = 1
 
for i in range(H):
    for j in range(W):
 
        #[0][0]の時は無視
        if (i == 0 and j == 0):
            continue
        #→の場合。一個前のマス。
        a = dp[i][j - 1]
        #↓の場合。一個前のマス。
        b = dp[i - 1][j]
 
        #.から#に移動するときだけ操作が(1回)必要
        if (L[i][j - 1] == "." and L[i][j] == "#"):
            a += 1
        if (L[i - 1][j] == '.' and L[i][j] == '#'):
            b += 1
 
        # min(dp[i][j],a,b)でもいいが結局問題になるのはa,bの比較だけでは？
        dp[i][j] = min(a, b)
 
print(dp[-1][-1])