import sys

if sys.platform =='ios':
	sys.stdin=open('Untitled.txt')
input = sys.stdin.readline
def MAP(): return [int(s) for s in input().split()]

n,m=MAP()
a=MAP()

#dp[price]=num of coins?

dp=[float('inf') for _ in range(n+1)]
dp[0]=0

for i in range(n+1):
	for j in a:
		if i+j <= n:
			dp[i+j]=min(dp[i]+1,dp[i+j])

print(dp[-1])
