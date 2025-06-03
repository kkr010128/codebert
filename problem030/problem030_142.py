import math
a,b,C=map(int,input().split())
radC=math.radians(C)
S=a*b*math.sin(radC)*(1/2)
c=a**2+b**2-2*a*b*math.cos(radC)
L=a+b+math.sqrt(c)
h=2*S/a
list=[S,L,h]
for i in list:
    print('{:.08f}'.format(i))
    

