# D - Redistribution
S = int(input())
MOD = 10**9+7

# dp[i]: 3 以上の数字で i を作る組み合わせ
dp = [0]*(S+1)

if S <= 2:
    print(0)
elif S <= 5:
    print(1)
else:
    # 初期条件
    dp[3],dp[4],dp[5] = 1,1,1

    # i を作る組合わせ
    for i in range(6,S+1):
        dp[i] = dp[i-2] + dp[i-3] + dp[i-4]

    ans = (dp[S])%MOD
    print(ans)