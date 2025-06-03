X = int(input())
# dp[i]:= ちょうどi円となる買い物が存在するorしない
dp = [0] * (X+1)
dp[0] = 1
for i in range(X):
    if dp[i] == 1:
        for next in [100,101,102,103,104,105]:
            if i+next<=X:
                dp[i+next] = 1
print(dp[X])