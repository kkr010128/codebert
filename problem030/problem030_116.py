a,b,c=map(int,input().split())
import math
d=math.sin(math.radians(c))
print(a*b*d/2)
e=math.cos(math.radians(c))
x=math.sqrt(a**2+b**2-2*a*b*e)
print(a+b+x)
print(2*(a*b*d/2)/a)
