import math

n = int(input())

point = [(0, 0), (100, 0)]

for i in range(n):
    len_point = len(point)
    tmp = []
    for j in range(len_point - 1):
        x1, y1 = point[j]
        x2, y2 = point[j+1]
        sx, sy = (2 * x1 + x2) / 3, (2 * y1 + y2) / 3
        tx, ty = (x1 + 2 * x2) / 3, (y1 + 2 * y2) / 3
        ux = (tx - sx) * math.cos(math.pi / 3) - (ty - sy) * math.sin(math.pi / 3) + sx
        uy = (tx - sx) * math.sin(math.pi / 3) + (ty - sy) * math.cos(math.pi / 3) + sy
        tmp.append((x1, y1))
        tmp.append((sx, sy))
        tmp.append((ux, uy))
        tmp.append((tx, ty)) 
    tmp.append((100, 0))
    point = tmp

for x, y in point:
    print(f"{x:.8f} {y:.8f}")
