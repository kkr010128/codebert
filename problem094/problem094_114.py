# -*- coding: utf-8 -*-
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

R, C, K = map(int, readline().split())

V = [[0]*(C+1) for _ in range(R+1)]
for i in range(K):
    r,c,v = map(int,readline().split())
    V[r][c] = v

dp = [0] * (C+1)
dp[0] = 0

for i in range(1,R+1):
    ndp = [0] * (C+1)
    row = V[i]
    ldp = [0] * 4
    for j in range(1,C+1):
        # ldp[0] = max(ldp[0], dp[j])
        ldp[0] = dp[j]
        for k in range(2,-1,-1):
            ldp[k+1] = max(ldp[k+1], ldp[k] + row[j]) # 取る場合と取らない場合
        ndp[j] = max(ldp)
    dp = ndp
print(dp[C])