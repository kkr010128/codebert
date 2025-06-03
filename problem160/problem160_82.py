# C Many Requirements

from itertools import combinations_with_replacement as com

N, M, Q = map(int, input().split())

C = []
for q in range(Q):
  C.append(tuple(map(int, input().split())))

As = com([i for i in range(1, M+1)], N)

ans = 0
for A in As:
  point = 0
  for Ci in C:
    if A[Ci[1]-1] - A[Ci[0]-1] == Ci[2]:
      point += Ci[3]
  ans = max(ans, point)

print(ans)