#!/usr/bin/env python3

while(True):
	try:
		a,b=map(int, input().split())
	except EOFError:
		break

	#euclidian algorithm	
	r=a%b
	x,y=a,b
	while(r>0):
		x=y
		y=r
		r=x%y
	gcd=y
	lcm=int(a*b/gcd)
	print("{0} {1}".format(gcd, lcm))