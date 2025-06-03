import math

a, b, c = map(float,input().split())
c = math.radians(c)
S = (1/2) * a * b * math.sin(c)

d = math.sqrt((a ** 2) + (b ** 2) - (2 * a * b * math.cos(c)))
L = a + b + d

H = (2 * S) / a

print(S,L,H)