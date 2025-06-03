import sys

r, c = [ int( val ) for val in sys.stdin.readline().split( " " ) ]
csums = [0]*c
rsum = 0
output = []
for k in range( r ):
	matrix = [ int( val ) for val in sys.stdin.readline().split( " " ) ]

	rsum = 0
	for i in range( c ):
		rsum += matrix[i]
		output.append( "{:d} ".format( matrix[i] ) )	
		csums[i] += matrix[i]
		
	output.append( "{:d}\n".format( rsum ) )

rsum = 0
for val in csums:
	rsum += val
	output.append( "{:d} ".format( val ) )	
	
output.append( "{:d}".format( rsum ) )
print( "".join( output ) )