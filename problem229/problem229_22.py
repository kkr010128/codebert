(H,N) = map(int,input().split())
l = []
for i in range(N):
    l.append([int(x) for x in input().split()])


dp = [10**10 for i in range(H+10**4+1)]
dp[0] = 0

for i in range(H+10**4+1):
    for j in range(N):
        if l[j][0] <= i:
            dp[i] = min(dp[i],dp[i-l[j][0]]+l[j][1])

ans = dp[H]
for i in range(1,10**4+1):
    ans = min(ans,dp[H+i])

print(ans)