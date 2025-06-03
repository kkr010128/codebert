import sys

a, b, c = [ int( val ) for val in sys.stdin.readline().split( ' ' ) ]
cnt = 0
i = a
while i <= b:
	if ( c % i ) == 0:
		cnt += 1
	i += 1
print( "{}".format( cnt ) )