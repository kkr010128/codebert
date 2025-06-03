H, W, K = map(int, input().split())
S = [input() for _ in range(H)]

C = [0] * W
for i in range(H):
  for j in range(W):
    if S[i][j] == "#":
      C[j] = 1
#print("C:", C)

U = [[0 for _ in range(W)] for _ in range(H)]
T = []

color = 1
for i in range(W):
  if C[i] == 1:
    T.append(i)
#print("T:", T)

for t in range(len(T)):
  if t == len(T) - 1:
    if t == 0:
      l = 0
    else:
      l = T[t]
    r = W
  else:
    if t == 0:
      l = 0
    else:
      l = T[t]
    r = T[t + 1]
  #print("l, r:", l, r)
  
  flag = 0
  for h in range(H):
    for w in range(l, r):
      if S[h][w] == "#":
        if flag == 0:
          flag = 1
        else:
          color += 1
    for w in range(l, r):
      U[h][w] = color
  color += 1

for h in range(H):
  print(*U[h])