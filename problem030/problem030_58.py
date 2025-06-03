import math
a,b,C=map(float,input().split())
C*=math.pi/180
print('%.8f'%(a*b*math.sin(C)/2))
print('%.8f'%(a+b+(a*a+b*b-2*a*b*math.cos(C))**.5))
print('%.8f'%(b*math.sin(C)))