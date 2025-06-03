N, M, Q = map(int, input().split())
cond = []
for i in range(Q):
  a, b, c, d = map(int, input().split())
  cond.append((a - 1, b - 1, c, d))

def dfs(A, head):
  if len(A) == N:
    score = 0
    for a, b, c, d in cond:
      if A[b] - A[a] == c:
        score += d
    return score
  ans = 0
  for n in range(head, M + 1):
    ans = max(ans, dfs(A + [n], n))
  return ans
print(dfs([1], 1))