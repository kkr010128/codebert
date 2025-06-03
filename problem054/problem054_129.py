import sys

n = int( sys.stdin.readline() )
s = [ False ] * 13
h = [ False ] * 13
c = [ False ] * 13
d = [ False ] * 13
for i in range( 0, n ):
	pattern, num = sys.stdin.readline().split( " " )
	if "S" == pattern:
		s[ int( num )-1 ] = True
	elif "H" == pattern:
		h[ int( num )-1 ] = True
	elif "C" == pattern:
		c[ int( num )-1 ] = True
	elif "D" == pattern:
		d[ int( num )-1 ] = True

for i in range( 0, 13 ):
	if not s[i]:
		print( "S {:d}".format( i+1 ) )
for i in range( 0, 13 ):
	if not h[i]:
		print( "H {:d}".format( i+1 ) )
for i in range( 0, 13 ):
	if not c[i]:
		print( "C {:d}".format( i+1 ) )
for i in range( 0, 13 ):
	if not d[i]:
		print( "D {:d}".format( i+1 ) )