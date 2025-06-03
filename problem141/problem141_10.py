import sys
input = sys.stdin.readline
from itertools import accumulate

n = int(input())
A = list(map(int, input().split()))
if n == 0:
  if A[0] == 1:
    print(1)
  else:
    print(-1)
  exit()
C = list(accumulate(A[::-1]))[::-1] + [0]
B = [-1]*(n+1)
B[0] = 1 - A[0]
for i in range(1, n+1):
  B[i] = min(C[i+1], 2*B[i-1]-A[i])
  if B[i] < 0 or B[i] < B[i-1] - A[i]:
    print(-1)
    exit()
ans = sum(A) + sum(B)
print(ans)