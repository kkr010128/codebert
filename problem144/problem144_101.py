import math
a,b,h,m = map(int,input().split())
x_h = a * math.sin(math.radians(0.5 * (60 * h + m)))
y_h = a * math.cos(math.radians(0.5 * (60 * h + m)))
x_m = b * math.sin(math.radians(6 * m))
y_m = b * math.cos(math.radians(6 * m))

print(math.sqrt((x_h-x_m)**2 + (y_h-y_m)**2))