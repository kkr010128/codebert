#(63)距離
import math
x1,y1,x2,y2=map(float,input().split())
a=abs(x2-x1)
b=abs(y2-y1)
c=math.sqrt(a**2+b**2)
print('{:.8f}'.format(c))
