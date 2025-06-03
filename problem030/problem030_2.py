a,b,C=map(float,input().split())
import math
S=0.5*a*b*math.sin(math.radians(C))
print('{:.8f}'.format(S))
print('{:.8f}'.format(a+b+math.sqrt(pow(a,2)+pow(b,2)-2*a*b*math.cos(math.radians(C)))))
print('{:.8f}'.format(S*2/a))

