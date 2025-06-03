import math
x1,y1,x2,y2=map(float,input().split())
x2=x2-x1
y2=y2-y1
x1,y1=0,0
dis=(x2**2+y2**2)
print(math.sqrt(dis))