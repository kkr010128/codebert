mod=998244353
n,k=map(int,input().split())
LR=[list(map(int,input().split())) for _ in range(k)]

DP=[0 for _ in range(n+1)]
SDP=[0 for _ in range(n+1)]
DP[1]=1
SDP[1]=1

for i in range(2,n+1):
    for l,r in LR:
        DP[i] +=(SDP[max(i-l,0)]-SDP[max(i-r,1)-1])%mod
        DP[i] %=mod
    SDP[i]=(SDP[i-1]+DP[i])%mod
print(DP[n])