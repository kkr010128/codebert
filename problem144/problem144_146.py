import math
a,b,h,m=map(int,input().split())
ang=min(abs(m*6-(h*30+m*0.5)),360-abs(m*6-(h*30+m*0.5)))
print((a**2+b**2-2*a*b*math.cos(math.radians(ang)))**0.5)