def gcd( x, y ):
	if 1 < y < x:
		return gcd( y, x%y )
	else:
		if y == 1:
			return 1
		return x

a, b = [ int( val ) for val in raw_input( ).split( " " ) ]
if a < b:
	a, b = b, a
print( gcd( a, b ) )