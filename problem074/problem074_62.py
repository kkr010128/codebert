import sys
readline = sys.stdin.readline

N,K = map(int,readline().split())
DIV = 998244353

L = [None] * K
R = [None] * K
for i in range(K):
  L[i],R[i] = map(int,readline().split())

dp = [0] * (N + 1)
sdp = [0] * (N + 1)
dp[1] = 1
sdp[1] = 1
  
for i in range(2, len(dp)):
  for j in range(K):
    li = max(i - R[j], 0)
    ri = i - L[j]
    if ri < 0:
      continue
    dp[i] += (sdp[ri] - sdp[li - 1])
    dp[i] %= DIV
  sdp[i] = sdp[i - 1] + dp[i]
  sdp[i] %= DIV
  
print(dp[N])