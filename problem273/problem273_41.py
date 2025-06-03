import sys 
import numpy as np
from collections import defaultdict
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N, K = map(int, readline().split())
A = [0] + list(map(int,readline().split()))
S = np.cumsum(A)
dic = defaultdict(int)
ans = 0
SS = [0] * (N+1)
for i in range(1,N+1):
    rem = (S[i]-i) % K
    SS[i] = rem

for i in range(N+1):
    if i >= K:
        dic[SS[i-K]] -= 1
    ans += dic[SS[i]]
    dic[SS[i]] += 1
print(ans)