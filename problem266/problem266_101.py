n=int(input())
dp=[0]*(10**5+1)
dp[100]=1
dp[101]=1
dp[102]=1
dp[103]=1
dp[104]=1
dp[105]=1
for i in range(106,10**5+1):
    if dp[i-100]==1:
        dp[i]=1
    elif dp[i-101]==1:
        dp[i]=1
    elif dp[i-102]==1:
        dp[i]=1
    elif dp[i-103]==1:
        dp[i]=1
    elif dp[i-104]==1:
        dp[i]=1
    elif dp[i-105]==1:
        dp[i]=1
print(dp[n])