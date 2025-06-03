a,b,c = map(float,input().split())
import math
h = b * math.sin(math.radians(c))
S = ( a * h ) / 2
L = a + b + ( math.sqrt( a**2 + b**2 - 2*a*b*math.cos(math.radians(c)) ) )
print('{0:.8f}'.format(S))
print('{0:.8f}'.format(L))
print('{0:.8f}'.format(h))
