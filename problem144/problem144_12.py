import math
A, B, H, M = map(int,input().split())

pi = math.pi
rad = pi * 2 * (H / 12 + (M / 60) / 12 - M / 60 )

length = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(rad))
print(length)