M=998244353
f=lambda:[*map(int,input().split())]
n,k=f()
lr=[f() for _ in range(k)]
dp=[0]*n
dp[0]=1
S=[0]
for i in range(1,n):
  S+=[S[-1]+dp[i-1]]
  for l,r in lr:
    dp[i]+=S[max(i-l+1,0)]-S[max(i-r,0)]
  dp[i]%=M
print(dp[-1])