import math
a,b,x=map(int,input().split())
if a*a*b==x:
    ans=90
elif x>((a**2)*b)/2:
    ans=math.degrees(math.atan(a/(2*(b-(x/(a**2))))))
else:
    ans=math.degrees(math.atan((2*x)/(a*(b**2))))
print(90-ans)
