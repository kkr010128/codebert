import sys

while True:
	line = sys.stdin.readline().rstrip()
	t = sum( [ int( line[i] ) for i in range( len( line ) ) ] )
	if 0 == t:
		break
	else:
		print( t )