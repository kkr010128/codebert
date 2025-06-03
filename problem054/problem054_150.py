import sys

n = int( sys.stdin.readline() )
cards = { pattern:[False]*13 for pattern in ( 'S', 'H', 'C', 'D' ) }
for i in range( n ):
	pattern, num = sys.stdin.readline().split( " " )
	cards[ pattern ][ int( num )-1 ] = True

for pattern in ( 'S', 'H', 'C', 'D' ):
	for i in range( 13 ):
		if not cards[ pattern ][ i ]:
			print( "{:s} {:d}".format( pattern, i+1 ) )