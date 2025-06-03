import sys

n, m, l = [ int( val ) for val in sys.stdin.readline().split( " " ) ]

matrixA = [ [ int( val ) for val in sys.stdin.readline().split( " " ) ] for row in range( n ) ]
matrixB = [ [ int( val ) for val in sys.stdin.readline().split( " " ) ] for row in range( m ) ]	
matrixC = [ [ sum( matrixA[i][k] * matrixB[k][j]  for k in range( m ) ) for j in range( l ) ] for i in range( n )  ]

for i in range( n ):
	print( " ".join( map( str, matrixC[i] ) ) )