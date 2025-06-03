import math
A, B, H, M = map(int,input().split())
#時針:0.5°/min
#分針:6.0°/min
print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(5.5 * (H * 60 + M) * math.pi / 180 )))