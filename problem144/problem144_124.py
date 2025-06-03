import math

A, B, H, M = map(int, input().split())

c = math.cos(math.radians(360 - abs(30 * H + 0.5 * M - 6 * M)))
X_2 = A ** 2 + B ** 2 - 2 * A * B * c
X = math.sqrt(X_2)

print(X)