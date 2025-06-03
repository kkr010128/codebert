# E - All-you-can-eat
n,t=map(int,input().split())
a,b=[],[]
for i in range(n):
    aa,bb=map(int,input().split())
    a.append(aa)
    b.append(bb)

dp1=[[0]*t for _ in range(n+1)] # 前から
dp2=[[0]*t for _ in range(n+1)] # 後ろから
arev=a[::-1]
brev=b[::-1]

for i in range(1,n+1):
    for j in range(t):
        if j-a[i-1]>=0:
            dp1[i][j]=max(dp1[i-1][j-a[i-1]]+b[i-1],dp1[i-1][j])
        else:
            dp1[i][j]=dp1[i-1][j]

for i in range(1,n+1):
    for j in range(t):
        if j-arev[i-1]>=0:
            dp2[i][j]=max(dp2[i-1][j-arev[i-1]]+brev[i-1],dp2[i-1][j])
        else:
            dp2[i][j]=dp2[i-1][j]

ans=-1
for i in range(1,n+1):
    for j in range(t):
        ans=max(ans,dp1[i-1][j]+dp2[n-i][t-1-j]+b[i-1])
print(ans)
