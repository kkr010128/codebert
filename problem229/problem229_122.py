import sys
input = sys.stdin.readline

h,n = map(int,input().split())
a = []
b = []
for i in range(n):
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)

dp = [10**10]*(h+1)
dp[0] = 0

for i in range(n):
    for j in range(h+1):
        dp[j] = min(dp[j],dp[max(0,j-a[i])]+b[i])
print(dp[h])