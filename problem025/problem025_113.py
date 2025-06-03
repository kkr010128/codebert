isExist = [False]*2001 
n = int( raw_input() )
A = [ int( val ) for val in raw_input().rstrip().split( ' ' ) ]
for i in A:
	for j in range( 2000-i, 0, -1 ):
		if isExist[j]:
			isExist[ i+j ] = True
	isExist[i] = True

q = int( raw_input() )
M = [ int( val ) for val in raw_input().rstrip().split( ' ' ) ]
for i in range( 0, q ):
	if isExist[ M[i] ]:
		print( "yes" )
	else:
		print( "no" )