import math

A, B, H, M = map(int, input().split())

deg_H = 360*(H+M/60)/12
deg_M = 360*M/60

theta = math.radians(abs(deg_H - deg_M))

ans = B**2 + A**2 - 2*A*B*math.cos(theta)

print(ans**0.5)
