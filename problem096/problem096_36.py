import math
n, d = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n)]
count = 0

for i in range(n):
    count = count + 1 if math.sqrt(xy[i][0]**2 + xy[i][1]**2) <= d else count

print(count)
