import math

A, B, H, M = list(map(lambda n: int(n), input().split(" ")))

thetaM = 6 * M
thetaH = 30 * H + 0.5 * M
theta = math.radians(180 - abs(abs(thetaH - thetaM) - 180))

print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(theta)))