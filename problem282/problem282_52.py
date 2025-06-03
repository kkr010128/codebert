import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

N,T = map(int,readline().split())
m = map(int,read().split())
AB = sorted(zip(m,m))

can_add = [0] * N
for n in range(N-1,0,-1):
    x = can_add[n]
    y = AB[n][1]
    can_add[n-1] = x if x > y else y

dp = np.zeros(T,np.int64)

answer = 0
for i,(a,b) in enumerate(AB):
    np.maximum(dp[a:], dp[:-a] + b, out = dp[a:])
    x = dp.max() + can_add[i]
    if answer < x:
        answer = x

print(answer)
