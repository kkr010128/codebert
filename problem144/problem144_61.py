import math
a,b,h,m=map(int,input().split())
res=min(abs(h*30+m/2-m*6),abs(h*30+m/2-m*6-360))
ans=a**2+b**2-2*a*b*math.cos(res*math.pi/180)
print(math.sqrt(ans))