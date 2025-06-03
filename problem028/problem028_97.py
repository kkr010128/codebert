N,M=list(map(int,input().split()))
C=list(map(int,input().split()))

dp = [[0]*len(C) for n in range(N+1)] #dp[n][c]

for n in range(1,N+1):
    dp[n][0] = n
    
for n in range(1,N+1):
    for c in range(1,len(C)):
        if C[c] > n:
            dp[n][c]=dp[n][c-1]
        else:
            dp[n][c]=min(dp[n][c-1],dp[n-C[c]][c]+1)
            
print(dp[-1][-1])
