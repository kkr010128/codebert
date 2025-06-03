S = int(input())
f = 10**9 + 7
dp = [0]*(S+1)
dp[0] = 1
for i in range(1,S+1):
    if i==1 or i==2: dp[i] = 0
    else:
        for j in range(0,i-2):
            dp[i] += dp[j]
            dp[i] %= f
print(dp[-1]%f)