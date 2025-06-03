n,k = list(map(int,input().split()))
A = list(map(int,input().split()))

if k == 1:exit(print(A[0]))
t = 0
dp = [-1] * n
dp[0] = 0
flg = 0
for i in range(1,k+1):
  t = A[t]-1
  if dp[t] != -1:
    flg = 1
    break
  dp[t] = i
if flg == 0:
  exit(print(t+1))
elif k == 2:
  exit(print(t+1))

l = i - dp[t]
K = (k-dp[t])%l + dp[t]

for i in range(n):
  if dp[i] == K:exit(print(i+1))


