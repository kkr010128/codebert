import sys

n, m, l = [ int( val ) for val in sys.stdin.readline().split( " " ) ]

matrixA = [ [ int( val ) for val in sys.stdin.readline().split( " " ) ] for row in range( n ) ]
matrixB = [ [ int( val ) for val in sys.stdin.readline().split( " " ) ] for row in range( m ) ]	
matrixC = [ [ 0 for row in range( l ) ] for row in range( n ) ]

output = []
for i in range( n ):
	for j in range( l ):
		for k in range( m ):
			matrixC[i][j] += ( matrixA[i][k] * matrixB[k][j] )
		output.append( "{:d}".format( matrixC[i][j] ) )
		output.append( " " )
	output.pop()
	output.append( "\n" )

output.pop()
print( "".join( output ) )