def main():
    S = int(input())
    dp = [0]*(S+1)
    dp[0] = 1
    dp[1] = 0
    if S >= 2:
        dp[2] = 0
    for i in range(3,S+1,1):
        for j in range(0,i-2,1):
            dp[i] += dp[j]

    return dp[S]%1000000007

print(main())
