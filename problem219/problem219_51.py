N = input()

keta = len(N)

dp = [[10**18 for i in range(2)] for j in range(keta)]

t = int(N[-1])

dp[0][0] = t
dp[0][1] = 10 - t

for i in range(keta - 2, -1, -1):
    
    t = int(N[i])
    #print(keta-i,i,t)
    dp[keta-i-1][0] = min(dp[keta-i-2][0]+t,dp[keta-i-2][1]+t+1)
    dp[keta-i-1][1] = min(dp[keta-i-2][0]+(10-t),dp[keta-i-2][1]+(10-(t+1)))
    #a, b = min(a + t, b + (t + 1)), min(a + (10 - t), b + (10 - (t + 1)))

#print(dp)

print(min(dp[keta-1][0],dp[keta-1][1]+1))