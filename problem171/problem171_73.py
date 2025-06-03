n,*a=map(int,open(0).read().split())
def dp_table(MXi,MXj):
    return [[0]*MXi for _ in range(MXj)] 
MX=2005
dp=dp_table(MX,MX)
p=sorted([(a[i]*MX+i) for i in range(n)])[::-1]
# print(p)
for i in range(n):
    ai,pi=divmod(p[i],MX)
    for l in range(n):
        r=i-l
        if not 0<=r<=n:
            break
        dp[i+1][l+1]=max(dp[i+1][l+1],dp[i][l]+ai*(pi-l))
        dp[i+1][l+0]=max(dp[i+1][l+0],dp[i][l]+ai*((n-r-1)-pi)) #??座標

ans=0
for i in range(n+1):
    ans=max(ans,dp[n][i])
print(ans)