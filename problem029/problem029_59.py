import math

x1,y1,x2,y2 = map(float,raw_input().split())
a = math.sqrt((x1-x2)**2+(y1-y2)**2)
print '%f'%a