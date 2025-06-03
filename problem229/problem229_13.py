h,n=map(int,input().split())
a,b=[],[]
for i in range(n):
    A,B=map(int,input().split())
    a.append(A)#ダメージ量
    b.append(B)#消費魔力

dp=[float('inf')]*(h+1)
dp[0]=0
for i in range(h):
    for j in range(n):

        next=i+a[j] if i+a[j]<=h else h
        dp[next]=min(dp[next],dp[i]+b[j])
print(dp[-1])
