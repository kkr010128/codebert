import math
rad = math.pi/180

A, B, H, M = map(int, input().split())
x = 6*M*rad
y = (60*H + M) * 0.5 * rad

print(math.sqrt(A**2 + B**2 -2*A*B*math.cos(x-y)))