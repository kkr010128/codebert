H, W, K = map(int, input().split())

S = [input() for i in range(H)]
C = [[0 for i in range(W)] for j in range(H)]
L = []
u = 0
M = []
for i in range(H):
  s = 0
  for j in range(W):
    if S[i][j] == '#':
      s += 1
      u += 1
      C[i][j] = u
  if s == 0:
    L.append(i)
  else:
    M.append(i)
d = 0
for i in range(len(M)):
  for j in range(W):
    if C[M[i]][j] != 0:
      for k in range(d, j):
        C[M[i]][k] = C[M[i]][j]
      d = j + 1
  for k in range(d, W):
    C[M[i]][k] = C[M[i]][d-1]
  d = 0
ma, mi = max(M), min(M)
M.insert(0, -1)
for i in range(W):
  for j in range(len(M)-1):
    for k in range(M[j]+1, M[j+1]):
      C[k][i] = C[M[j+1]][i]
  for j in range(ma+1, H):
    C[j][i] = C[ma][i]
for i in range(H):
  for j in range(W):
    if j != W-1:
      print(C[i][j], end = ' ')
    else:
      print(C[i][j], end = '')
  print()