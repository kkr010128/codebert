import math
a,b,x = map(int,input().split())

if b*a**2 == x:
	print(0)
	exit()

s = 2*x/(a*b)
if s < a:
	print(math.atan(b/s)/math.pi*180)
else:
	s = 2*b-2*x/(a**2)
	print(90-math.atan(a/s)/math.pi*180)