# pypy
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

R, C, K = map(int, readline().split())
rcv = list(map(int, read().split()))
rc2v = {}
for rr, cc, vv in zip(rcv[::3], rcv[1::3], rcv[2::3]):
    rc2v[(rr, cc)] = vv

dp = [[0]*4 for c in range(C+1)]
for r in range(1, R+1):
  for c in range(1, C+1):
    v = rc2v[(r, c)] if (r, c) in rc2v else 0
    dp[c][0] = max(dp[c-1][0], max(dp[c]))
    dp[c][1] = max(dp[c-1][1], dp[c][0] + v)
    for k in range(2, 4):
      dp[c][k] = max(dp[c-1][k], dp[c-1][k-1] + v)

print(max(dp[-1]))