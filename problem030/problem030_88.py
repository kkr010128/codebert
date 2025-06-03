#S, L, h
import math
a, b, C = map(int, input().split())

S = a*b*math.sin(C*math.pi/180)*(1/2)
L = a+b+math.sqrt(a*a+b*b-2*a*b*math.cos(C*math.pi/180))
h = 2*S/a

print('%.4f'% S)
print('%.4f'% L)
print('%.4f'% h)