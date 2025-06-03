from collections import deque

def getMaxDistance(s,startY,startX):
  d = deque()
  distances = [[0 for _ in range(w)] for j in range(h)]
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]
  maxDistance = 0
  d.append(startX)
  d.append(startY)
  while d:
    x = d.popleft()
    y = d.popleft()
    if s[y][x]=='#': continue
    maxDistance = max(maxDistance, distances[y][x])
    for i in range(4):
      xx = x + dx[i]
      yy = y + dy[i]
      if not (0 <= yy < h and 0 <= xx < w): continue
      if s[yy][xx] != '.': continue
      if distances[yy][xx] != 0: continue
      if xx == startX and yy == startY: continue
      d.append(xx)
      d.append(yy)
      distances[yy][xx] = distances[y][x] + 1
  return maxDistance

h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
maxDistance = 0
for i in range(h):
  for j in range(w):
    maxDistance = max(maxDistance, getMaxDistance(s,i,j))
print(maxDistance)