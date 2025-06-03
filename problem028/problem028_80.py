inf=10**9
n,m=map(int,input().split())
C=list(map(int,input().split()))

DP=[inf]*(n+1)
DP[0]=0
for i in range(n+1):
    for c in C:
        if 0<=i+c<=n:
            DP[i+c]=min(DP[i+c],DP[i]+1)
print(DP[n])
