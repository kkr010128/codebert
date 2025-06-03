from itertools import combinations_with_replacement as cwr

N, M, Q = map(int, input().split())
abcd = [list(map(int, input().split())) for i in range(Q)]

def calc_score(A):
  score = 0
  for a, b, c, d in abcd:
    if A[b-1] - A[a-1] == c:
      score += d
  return score

ans = 0
for A in cwr([i for i in range(1, M+1)], N):
  ans = max(ans, calc_score(A))

print(ans)