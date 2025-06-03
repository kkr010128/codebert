n,k=map(int,input().split())
s=[]
s2=[]
mod=998244353

for i in range(k):
    l,r=map(int,input().split())
    s+=[i for i in range(l,r+1)]
    s2.append([l,r])
s.sort()
dp=[0]*(n+1)
dpsum=[0]*(n+1)
dp[1]=1
dpsum[1]=1
for i in range(2,n+1):
    for j in range(k):
        if i-s2[j][0]>=0:
            dp[i]+=(dpsum[i-s2[j][0]]-dpsum[max(i-s2[j][1],1)-1])%mod
            dp[i]%=mod
    dpsum[i]=(dpsum[i-1]+dp[i])%mod
print(dp[n])
