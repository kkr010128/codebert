import numpy as np
 
N = int(input())
 
 
def divisor(N):
    x = np.arange(1, int(N**(1/2))+1, dtype=np.int64)
    div = set(x[N % x == 0])
    return div | set(N // x for x in div)
 
 
cand = divisor(N) | divisor(N - 1)
 
 
def test(N, K):
    if K == 1:
        return False
    while N % K == 0:
        N //= K
    return N % K == 1
 
 
answer = sum(test(N, d) for d in cand)
print(answer)