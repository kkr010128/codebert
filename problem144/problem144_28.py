import math

a,b,h,m=map(int,input().split())

hc=360/12*h+30/60*m #時針の角度
mc=360/60*m #分針の角度
hm=abs(hc-mc) #時針と分針の角度の差
if hm > 180:
    hm=360-hm

mcos=math.cos(math.radians(hm))
c=a**2+b**2-(2*a*b*mcos) #余剰定理

print(math.sqrt(c))