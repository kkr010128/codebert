import math

px, py, qx, qy = map(float,input().split())
pq = (qx - px) ** 2 + (qy - py) ** 2

print(math.sqrt(pq))


