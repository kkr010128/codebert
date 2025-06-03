import math

a, b, h, m = map(int, input().split())
st = (60*h+m)/360*math.pi
lt = m/30*math.pi
sx = a*math.sin(st)
sy = a*math.cos(st)
lx = b*math.sin(lt)
ly = b*math.cos(lt)
print(math.sqrt((lx-sx)**2+(ly-sy)**2))
