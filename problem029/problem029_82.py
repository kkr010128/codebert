import math
x1,y1,x2,y2 = map(float,raw_input().split(' '))
x = abs(x1-x2);
y = abs(y1-y2);
a = math.sqrt(x**2 + y**2) 
print a