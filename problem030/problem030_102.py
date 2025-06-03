import math
a, b, deg = map(float, raw_input().split(" "))

c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(deg)))
L = a + b + c
s = (a + b + c) / 2.0
S = math.sqrt(s*(s-a)*(s-b)*(s-c))
h = 2 * S / a

print(str(S) + " " + str(L) + " " + str(h))