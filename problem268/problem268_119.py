N = int(input())
a = list(map(int,input().split()))
dp = [[-1,-1,-1,1] for _ in range(N+1)]
for i in range(N):
    check = dp[i][:3]
    pattern = check.count(a[i]-1)
    dp[i+1][3] *= dp[i][3]*pattern
    dp[i+1][3] = dp[i+1][3]%1000000007
    for k in range(3):
        dp[i+1][k]= dp[i][k]
    if dp[i][0]== a[i]-1:
        dp[i+1][0] = a[i]
    elif dp[i][1] ==a[i]-1:
        dp[i+1][1] = a[i]
    elif dp[i][2] ==a[i]-1:
        dp[i+1][2] = a[i]
print(dp[N][3])