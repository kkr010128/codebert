import math

A, B, H, M = map(int, input().split())

theta = math.radians(30 * H - 5.5 * M)

ans = math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(theta))

print(ans)