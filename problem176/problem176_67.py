import sys 
import numpy as np
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
MOD = 10 ** 9 + 7    
N, K = map(int, readline().split())
d = [0] * (K+1)
for i in range(K,0,-1):
    t = K // i
    cnt = pow(t,N,MOD)
    for j in range(2,t+1):
        cnt -= d[i*j]
        cnt %= MOD
    d[i] = cnt
ans = 0
for num,cnt in enumerate(d):
    ans += num * cnt
    ans %= MOD
print(ans) 