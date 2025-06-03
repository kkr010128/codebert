import math
a,b,c=map(int,input().split())

s=0.5*a*b*math.sin(math.radians(c))
l=a+b+math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(c)))
h=b*math.sin(math.radians(c))

print("%.6f %.6f %.6f"%(s,l,h))