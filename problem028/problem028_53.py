n,m=map(int,input().split())
c=list(map(int,input().split()))
c.sort(reverse=True)
#print(c)

dp=[0]
for i in range(1,n+1):
    mini=float("inf")
    for num in c:
        if i-num>=0:
            mini=min(mini,dp[i-num]+1)
    dp.append(mini)

#print(dp)
print(dp[-1])
