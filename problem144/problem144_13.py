import math

A, B, H, M = map(int, input().split())
h_rad = (H / 12 + M / 12 / 60)* 2 * math.pi
m_rad = M / 60 * 2 * math.pi
dif_rad = abs(h_rad - m_rad)
ans = math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(dif_rad))
print(ans)