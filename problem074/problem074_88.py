N,K=map(int,input().split())
x=998244353
dp=[0 for i in range(N)]
sdp=[0 for i in range(N)]
L=[]
R=[]
dp[0]=1
sdp[0]=1
for i in range(K):
    l,r=map(int,input().split())
    L.append(l)
    R.append(r) 
for i in range(1,N):
    for j in range(K):
        dp[i]+=(sdp[max(i-L[j],-1)]-sdp[max(i-R[j]-1,-1)])
        dp[i]%=x
    sdp[i]=(sdp[i-1]+dp[i])%x
print(dp[-1]%x)