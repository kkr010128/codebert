import itertools
import numpy as np
d_list = []
sum_d = 0
N, M, Q = map(int, input().split())
abcd = [list(map(int, input().split())) for i in range(Q)]
ans = 0
A = [1 for i in range(N)]
for A in itertools.combinations_with_replacement(range(1, M+1), N):
  for i in range(Q):
    if A[abcd[i][1]-1]-A[abcd[i][0]-1] == abcd[i][2]:
      d_list.append(abcd[i][3])
  if sum_d <= sum(d_list):
    sum_d = sum(d_list)
  d_list.clear()
print(sum_d)