h,n = map(int,input().split())
a = [0]*n
b = [0]*n
for i in range(n): a[i],b[i] = map(int,input().split())
dp = [10**9]*(h+1)
dp[0] = 0
for i in range(h):
    for j in range(n):
        dp[min(i+a[j],h)] = min(dp[min(i+a[j],h)],dp[i]+b[j])
print(dp[h])