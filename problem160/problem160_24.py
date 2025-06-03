import itertools
import numpy as np

N, M, Q = map(int, input().split())
abcd = [list(map(int, input().split())) for i in range(Q)]

score = []
ans = 0
for A in itertools.combinations_with_replacement(range(1, M+1), N):
  for i in range(Q):
    a = abcd[i][0]
    b = abcd[i][1]
    c = abcd[i][2]
    d = abcd[i][3]
    if A[b-1]-A[a-1] == c:
      score.append(d)
  if ans <= sum(score):
    ans = sum(score)
  score.clear()
print(ans)