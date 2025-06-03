import math
a,b,c=map(int,input().split())
s=a/2*b*math.sin(math.radians(c))
l=a+b+math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(c)))
h=b*math.sin(math.radians(c))
print('{:.5f}\n{:.5f}\n{:.5f}'.format(s,l,h))
