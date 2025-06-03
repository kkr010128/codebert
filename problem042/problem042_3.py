import sys

i=1
while True:
	x = int( sys.stdin.readline() )
	if 0 != x:
		print( "Case {}: {}".format( i, x) )
	else:
		break
	i += 1