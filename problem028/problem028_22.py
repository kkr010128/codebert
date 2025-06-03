n,m=map(int,input().split())
C=list(map(int,input().split()))

inf=float('inf')

DP=[[inf]*(n+1) for i in range(m+1)]

DP[0][0]=0

for i in range(m):
	for j in range(n+1):
		if j-C[i]<0:
			DP[i+1][j]=DP[i][j]
		else:
			DP[i+1][j]=min(DP[i][j],DP[i+1][j-C[i]]+1)

print(DP[m][n])
