import math

a,b,deg = map(float,input().split(" "))

sindeg = math.sin(math.radians(deg))
S = (a*b*sindeg)/2


cosdeg = math.cos(math.radians(deg))
z = a*a + b*b - 2*a*b*cosdeg
L = a + b + math.sqrt(z)

h = b*sindeg

print("{:.5f}".format(S))
print("{:.5f}".format(L))
print("{:.5f}".format(h))


