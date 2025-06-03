from math import log2
N = int(input())
log = int(log2(N)+1)
ans = (2**log-1)
print(ans)