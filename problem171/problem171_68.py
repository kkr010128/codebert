n,*a=map(int,open(0).read().split())
dp=[[0]*(n+1)for _ in range(n+1)]
for t,(c,k) in enumerate(sorted((c,k) for k,c in enumerate(a))[::-1]):
	for i in range(t+1):
		j=t-i
		if dp[i+1][j]<dp[i][j]+c*abs(i-k):dp[i+1][j]=dp[i][j]+c*abs(i-k)
		if dp[i][j+1]<dp[i][j]+c*abs(n-1-k-j):dp[i][j+1]=dp[i][j]+c*abs(n-1-k-j)
print(max(dp[i][~i]for i in range(n+1)))