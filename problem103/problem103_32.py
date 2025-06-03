N = int(input())
An = list(map(int, input().split()))
dp = [0 for x in range(N+10)]
dp[0] = 1000
for i in range(1, N):
    stock = dp[i-1] // An[i-1]
#     print(dp[i-1], An[i-1], stock)
    money = dp[i-1]
    money -= stock * An[i-1]
    money += stock * An[i]
#     print(money)
    dp[i] = max(dp[i-1], money)
print(dp[N-1])  