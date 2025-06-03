n,k=map(int,input().split())
k_list=[]

for i in range(k):
    l,r=map(int,input().split())
    k_list.append([l,r])

dp=[0]*(n+1)
dp[1]=1
dpsum=[0]*(n+1)
dpsum[1]=1

for i in range(1,n):
    dpsum[i]=dp[i]+dpsum[i-1]
    for j in range(k):
        l,r=k_list[j]
        li=i+l
        ri=i+r+1
        if li<=n:
            dp[li]+=dpsum[i]
            dp[li]=dp[li]%998244353
        if ri<=n:
            dp[ri]-=dpsum[i]
            dp[ri]=dp[ri]%998244353

print(dp[n])
