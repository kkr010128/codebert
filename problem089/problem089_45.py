h, w, m = map(int, input().split())

bomb = []
cnth = [0 for i in range(h)]
cntw = [0 for i in range(w)]
bomh = [set() for i in range(h)]
bomw = [set() for i in range(w)]
for i in range(m):
  x, y = map(int, input().split())
  x -= 1
  y -= 1
  cnth[x] += 1
  cntw[y] += 1
  bomh[x].add(y)
  bomw[y].add(x)
  bomb.append([x,y])
maxh = max(cnth)
maxw = max(cntw)
ans = maxh + maxw - 1

xx = []
yy = []
for i in range(h):
  if maxh == cnth[i]:
    xx.append(i)
for i in range(w):
  if maxw == cntw[i]:
    yy.append(i)

for i in xx:
  for j in yy:
    if j not in bomh[i]:
      print (ans+1)
      exit()
print (ans)