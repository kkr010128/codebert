A, B, H, M = map(int, input().split())

import math

theta = (30 * H) - (5.5 * M)

d2 = A * A + B * B - 2 * A * B * math.cos(math.radians(theta))

d = math.sqrt(d2)

print(d)
