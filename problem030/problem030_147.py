import math
a, b, C = map(int, input().split())
print('{0:.4f}'.format(0.5*a*b*math.sin(math.radians(C))))
L = (a+b) + math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(C)))
print(L)
print('{0:.4f}'.format(math.sin(math.radians(C)) * b))

