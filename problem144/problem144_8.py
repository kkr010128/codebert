import math
a, b, h, m = map(int,input().split())

ax = a*math.cos(math.radians(90-360/12*(h+m/60)))
ay = a*math.sin(math.radians(90-360/12*(h+m/60)))

bx = b*math.cos(math.radians(90-360/60*m))
by = b*math.sin(math.radians(90-360/60*m))

print(math.sqrt((ax-bx)**2+(ay-by)**2))
