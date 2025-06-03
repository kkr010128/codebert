import math
A, B, H, M = map(int, input().split())
a = math.pi/360 * (H*60 + M)
b = math.pi/30 * M
# if abs(a - b) > math.pi:
#     theta = 2 * math.pi - abs(a-b)
# else:
theta = abs(a-b)
L = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(theta))
print(L)