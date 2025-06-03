N = int(input())

def f(l, r):
  cnt = 0
  if l == r and l <= N:
    cnt += 1
  if l*10 + r <= N:
    cnt += 1
  for c in range(1, 5):
    x = l*10**(c+1) + r
    i = 0
    I = int("9"*c)
    while x <= N and i <= I:
      cnt += 1
      x += 10
      i += 1
  return cnt

C = [[0]*9 for _ in range(9)]
ans = 0

for i in range(9):
  for j in range(9):
    C[i][j] = f(i+1, j+1)

for i in range(9):
  for j in range(9):
    ans += C[i][j] * C[j][i]

print(ans)