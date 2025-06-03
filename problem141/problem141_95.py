n,*a=map(int,open(0).read().split())
dp=[0]*(n+1)
dp[0]=1
for i,x in enumerate(a):
	if dp[i]<x:
		print(-1)
		exit()
	if i<n:
		dp[i+1]=(dp[i]-x)*2
dp[-1]=a[-1]
for i in range(n,0,-1):
	if dp[i-1]>a[i-1]+dp[i]:
		dp[i-1]=a[i-1]+dp[i]
print(sum(dp))