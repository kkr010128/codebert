h,n=map(int, input().split())
a=[0]*n
b=[0]*n
for i in range(n):
    a[i],b[i]=map(int,input().split())
max_a=max(a)
dp=[float("inf")]*(h+max_a+1)
dp[0]=0
for i in range(h):
    for j in range(n):
        dp[i+a[j]] = min(dp[i+a[j]], dp[i]+b[j])
print(min(dp[h:]))