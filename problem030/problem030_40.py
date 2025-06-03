import math

a,b,c=(int(x) for x in input().split())
s=1/2*a*b*math.sin(c/180*math.pi)
l=math.sqrt(a**2+b**2-2*a*b*math.cos(c/180*math.pi))+a+b
h=s/a*2
print('{:.05f}'.format(s))
print('{:.05f}'.format(l))
print('{:.05f}'.format(h))

