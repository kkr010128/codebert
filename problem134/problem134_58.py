import numpy as np
N = int(input())
A = list(map(int, input().split()))
ans = 1
if 0 in A:
  ans = 0
for i in range(N):
  ans *= A[i]
  if ans > 1000000000000000000:
    ans = -1
    break
print(ans)
