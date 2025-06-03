r, c = map(int, input().split())
tbl = [[] for _ in range(r)]
cSum = [0 for _ in range(c+1)]

for i in range(r):
  tblS = input()
  tbl[i] = list(map(int, tblS.split()))
  print(tblS, end = '')
  print(' ', sum(tbl[i]), sep = '')

  for j in range(c):
    cSum[j] += tbl[i][j]
  cSum[c] += sum(tbl[i])

print(' '.join(map(str, cSum)))
