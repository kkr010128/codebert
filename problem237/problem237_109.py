n = int(input())
arm = []
for i in range(n):
    x , l = map(int,input().split())
    arm.append([x,l])
arm.sort()
dp = [[0,0] for i in range(n)]
dp[0][1] = arm[0][0] + arm[0][1]
for i in range(1,n):
    if dp[i-1][1] <= arm[i][0] -arm[i][1]:
        dp[i][0] = dp[i-1][0]
        dp[i][1] = arm[i][0] + arm[i][1]
    else:
        dp[i][0] = dp[i-1][0] + 1
        dp[i][1] = min(arm[i][0] + arm[i][1],dp[i-1][1])
        
print(n-dp[n-1][0])