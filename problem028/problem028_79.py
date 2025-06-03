n,m=map(int,raw_input().split())
c=map(int,raw_input().split())

dp=[i for i in range(n+1)]

c.remove(1)
c.sort()

for coin in c:
	for x in range(1,n+1):
		if x-coin>=0:
			dp[x]=min(dp[x],dp[x-coin]+1)

print dp[n]
