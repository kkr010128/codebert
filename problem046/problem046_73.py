import math

r = float(input())

S = math.pi * r * r
L = 2 * math.pi * r

print("{0:.10f}".format(S),end=" ")
print("{0:.10f}".format(L))