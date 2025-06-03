isExist = [0]*2001 
n = int( input() )
A = [ int( val ) for val in input().rstrip().split( ' ' ) ]
for i in A:
	for j in range( 2000-i, 0, -1 ):
		if 1 == isExist[j]:
			isExist[ i+j ] = 1
	isExist[i] = 1

q = int( input() )
M = [ int( val ) for val in input().rstrip().split( ' ' ) ]
for i in range( 0, q ):
	if 1 == isExist[ M[i] ]:
		print( "yes" )
	else:
		print( "no" )