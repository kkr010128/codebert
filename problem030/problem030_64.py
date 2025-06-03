import math

a, b, C = map(int, raw_input().split())

S = a * b * math.sin(math.radians(C)) / 2
L = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(C))) + a + b
h = 2*S/a

print S
print L
print h