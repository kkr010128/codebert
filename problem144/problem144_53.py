import math
A, B, H, M = map(int, input().split(' '))
deg = abs(30 * H + 0.5 * M - 6 * M)
if deg >180:
    deg = 360 - deg
deg = math.radians(deg)
print(math.sqrt((B - A * math.cos(deg)) ** 2 + (A * math.sin(deg)) ** 2))