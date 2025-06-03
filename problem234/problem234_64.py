#同値なものはリストでまとめる

n = int(input())
c = [[[] for i in range(9)] for i in range(9)]

for i in range(1,n+1):
  s = str(i)
  if s[-1] == '0':
    continue
  c[int(s[0])-1][int(s[-1])-1].append(i)

ans = 0

for i in range(9):
  for j in range(9):
    ans += len(c[i][j])*len(c[j][i])

print(ans)