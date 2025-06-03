n, m, q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]
a,b,c,d = [],[],[],[]
for i in range(q):
  a.append(abcd[i][0])
  b.append(abcd[i][1])
  c.append(abcd[i][2])
  d.append(abcd[i][3])

def score(A):
  tmp = 0
  for ai, bi, ci, di in zip(a, b, c, d):
      if A[bi] - A[ai] == ci:
          tmp += di
  return tmp

def dfs(A):
  if len(A)==n+1:
    return score(A)
  ans = 0
  for i in range(A[-1],m):
    A.append(i)
    ans = max(ans,dfs(A))
    A.pop()
  return ans

print(dfs([0]))