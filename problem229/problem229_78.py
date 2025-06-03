h,n=map(int,input().split())
A=[]
B=[]
for i in range(n):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

dp=[10**10 for i in range(h+1)]

dp[h]=0

for i in reversed(range(1,h+1)):
    for j in range(n):
        if i-A[j]>=0:
            dp[i-A[j]]=min(dp[i-A[j]],dp[i]+B[j])
        else:
            dp[0]=min(dp[0],dp[i]+B[j])

print(dp[0])