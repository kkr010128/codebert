import itertools
n,m,q = list(map(int, input().split()))
abcd = [[0] * 4 for _ in range(q)]
for i in range(q):
  abcd[i] = list(map(int, input().split()))

M = itertools.combinations_with_replacement(range(m),n)
ans = 0
for A in M:
  for i in range(1,n):
    if A[i] <= A[i-1]:break
  temp = 0
  for i in range(q):
    a = A[abcd[i][0]-1]
    b = A[abcd[i][1]-1]
    c = abcd[i][2]
    d = abcd[i][3]
    if b - a == c:
      temp += d
  ans = max(ans,temp)

print(ans)