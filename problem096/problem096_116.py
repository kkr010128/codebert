import math

N, D = map(int,input().split())
XY = list(list(map(int,input().split())) for _ in range(N))

count = 0
for i in range(N):
  if math.sqrt(XY[i][0] ** 2 + XY[i][1] ** 2) <= D: count += 1

print(count)