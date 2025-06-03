import math

while True:
	try:
		a,b=list(map(int,input().split()))
		x=math.gcd(a,b)
		y=int(a*b/x)
		print("%d %d"%(x,y))
	except:
		break
