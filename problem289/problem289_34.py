import math
a,b,x=map(int,input().split())
if x>=(1/2)*a**2*b:
  k=2*(a**2*b-x)/a**3
  print(math.degrees(math.atan(k)))
else:
  j=2*x/(a*b**2)
  print(90-math.degrees(math.atan(j)))