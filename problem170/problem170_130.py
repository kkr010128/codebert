#D
from collections import deque
N,K = map(int,input().split())
numbers = [i for i in range(0,N+1)]
large  = deque([N])
small = deque([0])
for i in range(1,N+1):
    large.append(large[-1]+numbers[-i-1])
    small.append(small[-1]+numbers[i])

mod = 10**9+7

ans = 1
for i in range(K,N+1):
    ans += (large[i-1] - small[i-1] + 1)%mod
print(ans%mod)