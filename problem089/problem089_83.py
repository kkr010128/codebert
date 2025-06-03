H, W, M = map(int, input().split())
X = [0 for i in range(H)]
Y = [0 for j in range(W)]
s = set([])
for i in range(M):
  h, w = map(int, input().split())
  X[h-1] += 1
  Y[w-1] += 1
  s.add((h-1, w-1)) #タプルを使う
mX = max(X)
mY = max(Y)
I = [i for i in range(H) if X[i] == mX]
J = [j for j in range(W) if Y[j] == mY]
flag = 0
for i in I:
  for j in J:
    if {(i, j)} <= s:
      continue
    flag = 1
    print(mX+mY)
    break
  if flag == 1:
    break
if flag == 0:
  print(mX+mY-1)