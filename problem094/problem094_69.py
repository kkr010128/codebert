R, C, K = map(int, input().split())
# = int(input())
p = []
for k in range(K):
  p.append(list(map(int, input().split())))

maps = [[0 for _ in range(C)] for _ in range(R)]
for k in range(K):
  maps[p[k][0]-1][p[k][1]-1] += p[k][2]

point1 = [[0 for _ in range(C)] for _ in range(R)]
point2 = [[0 for _ in range(C)] for _ in range(R)]
point3 = [[0 for _ in range(C)] for _ in range(R)]

point1[0][0] = maps[0][0]

for r in range(R):
  for c in range(C):
    a, b, d = point1[r][c], point2[r][c], point3[r][c]  
    if c < C - 1:
      x = maps[r][c+1]
      point1[r][c+1] = max(point1[r][c+1], x, a)
      point2[r][c+1] = max(point2[r][c+1], a + x, b)
      point3[r][c+1] = max(point3[r][c+1], b + x, d)
    if r < R - 1:
      point1[r+1][c] = maps[r+1][c] + max(a, b, d)


print(max(point1[-1][-1], point2[-1][-1], point3[-1][-1]))