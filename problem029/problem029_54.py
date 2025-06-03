import math
x1,y1,x2,y2 = map(float,input().split())
x = (x1-x2)**2
y = (y1-y2)**2
print('{:.8f}'.format(math.sqrt(x+y)))
