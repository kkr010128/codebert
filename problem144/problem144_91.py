import math

A, B, H, M = map(int, input().split())

A_degree = (360 / (60 * 12)) * (H * 60 + M)
B_degree = (360 / 60) * M

A_x = A * math.cos(math.radians(A_degree))
A_y = A * math.sin(math.radians(A_degree))

B_x = B * math.cos(math.radians(B_degree))
B_y = B * math.sin(math.radians(B_degree))

ans = math.sqrt((A_x - B_x)**2 + (A_y - B_y)**2)

print(ans)