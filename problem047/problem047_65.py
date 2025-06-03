import sys

while True:
	a, op, b = sys.stdin.readline().split( " " )
	if "?" == op:
		break
	a = int( a )
	b = int( b )
	if "+" == op:
		print( "{:d}".format( a+b ) )
	elif "-" == op:
		print( "{:d}".format( a-b ) )
	elif "*" == op:
		print( "{:d}".format( a*b ) )
	elif "/" == op:
		print( "{:d}".format( a//b ) )