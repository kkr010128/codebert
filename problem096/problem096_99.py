import math

N, D = map(int, input().split())
XY = []
for _ in range(N):
    x, y = map(int, input().split())
    XY.append([x,y])

cnt = 0
for xy in XY:
    if math.sqrt(pow(xy[0], 2) + pow(xy[1], 2)) <= D:
        cnt += 1
print(cnt)

