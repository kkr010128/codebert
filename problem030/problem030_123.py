import math

a, b, C = map(float, input().split(' '))

rad = math.radians(C)
c = math.sqrt(a**2+b**2-2*a*b*math.cos(rad))

S = a*b*math.sin(rad)*1/2
L = a+b+c
h = abs(b*math.sin(rad))

print('{:.5f} {:.5f} {:.5f}'.format(S, L, h))