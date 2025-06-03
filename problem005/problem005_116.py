import sys

while True:
    try:
	a,b = map(int,raw_input().split())
	tempa = a
	tempb = b
	while tempa % tempb != 0 :
	    tempa , tempb = (tempb,tempa%tempb)
	gcd = tempb
	lcm = a * b / gcd
	print "%d %d" % ( gcd, lcm)
	

    except EOFError:
	break