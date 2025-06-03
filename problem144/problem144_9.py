import math
A,B,H,M=map(int,input().split())
b=30*H+30*(M/60)
c=6*M
d=math.fabs(b-c)
d=math.radians(d)
f=0

f=A**2+B**2-2*A*B*(math.cos(d))
print(math.fabs(math.sqrt(f)))
