
N,K=map(int,input().split())
L=[0]*K
R=[0]*K
for i in range(K):
    L[i],R[i]=map(int,input().split())
    
MOD=998244353
dp=[0]*(N+1)
dpsum=[0]*(N+1)
dp[1]=1
dpsum[1]=1

for i in range(2,N+1):
    for j in range(K):
        Li=i-R[j]
        Ri=i-L[j]

        if Ri<0:
            continue
        else:
            Li=max(Li,1)
            dp[i]=(dp[i]+dpsum[Ri]-dpsum[Li-1])%MOD
    
    dpsum[i]=dpsum[i-1]+dp[i]

print(dp[N])