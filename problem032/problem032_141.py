import math

def getDistance( x, y, n, p ):
	dxy = 0
	for i in range( n ):
		dxy += abs( x[i] - y[i] )**p
	return dxy**(1/float( p ) )


n = int( raw_input() )
x = [ float( i ) for i in raw_input( ).split( " " ) ]
y = [ float( i ) for i in raw_input( ).split( " " ) ]
print( getDistance( x, y, n, 1 ) )
print( getDistance( x, y, n, 2 ) )
print( getDistance( x, y, n, 3 ) )
dxy = [ 0 ]*(n+1)
for i in range( n ):
	dxy[i] = abs( x[i] - y[i] )

print( max( dxy ) )