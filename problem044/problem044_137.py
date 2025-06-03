import sys

a, b, c = [ int( val ) for val in sys.stdin.readline().split( " " ) ]
cnt = 0
for i in range( a, b+1 ):
	if 0 == c%i:
		cnt += 1
print( "{}".format( cnt ) )