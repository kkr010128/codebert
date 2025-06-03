import sys

n = int( sys.stdin.readline() )
cards = { 'S': [ False ] * 13, 'H': [ False ] * 13, 'C': [ False ] * 13, 'D': [ False ] * 13 }
for i in range( n ):
	pattern, num = sys.stdin.readline().split( " " )
	if "S" == pattern:
		cards[ 'S' ][ int( num )-1 ] = True
	elif "H" == pattern:
		cards[ 'H' ][ int( num )-1 ] = True
	elif "C" == pattern:
		cards[ 'C' ][ int( num )-1 ] = True
	elif "D" == pattern:
		cards[ 'D' ][ int( num )-1 ] = True

for pattern in ( 'S', 'H', 'C', 'D' ):
	for i in range( 13 ):
		if not cards[ pattern ][ i ]:
			print( "{:s} {:d}".format( pattern, i+1 ) )