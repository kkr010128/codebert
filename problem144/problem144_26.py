import math
a,b,h,m=map(int,input().split())


f=h / 12 * 360 - m / 60 * 360 + m / 60 / 12 * 360


theta=math.radians(f)
print(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(theta)))