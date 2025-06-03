import math
x1,y1,x2,y2=map(float,input().split())
a=(x2-x1)**2+(y2-y1)**2
l=math.sqrt(a)
print(f'{l:.8f}')
