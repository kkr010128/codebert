# -*- coding: utf-8 -*-
import sys 
from itertools import accumulate
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N, K = map(int, readline().split())
P = [0] + list(map(int,readline().split()))
C = [0] + list(map(int,readline().split()))

ans = -10 ** 10
for i in range(1,N+1):
    l = 1
    j = P[i]
    s = C[j]
    ans = max(ans, s) #iを始まりとして
    while j != i:     # 1周期もしないときの最大値
        j = P[j]
        s += C[j]
        l += 1
        if K >= l:
            ans = max(ans, s)
    
    c = 1
    j = P[j]
    t = C[j]
    ans = max(ans, t + ((K - c) // l) * s) # 1回と周期分
    
    while j != i:
        j = P[j]
        t += C[j]
        c += 1
        if K >= c:
            ans = max(ans, t + ((K - c) // l) * s) # c回と周期分
print(ans)