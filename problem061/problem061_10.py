import sys

line = sys.stdin.readline()
output = []
for i in range( len( line )-1 ):
	c = ord( line[i] )
	if ord( 'a' ) <= c and c <= ord( 'z' ):
		c = chr( c ).upper()
	elif ord( 'A' ) <= c and c <= ord( 'Z' ):
		c = chr( c ).lower()
	else:
		c = chr( c )
	output.append( c )

print( "".join( output ) )