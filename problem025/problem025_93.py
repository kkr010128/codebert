def solve( p, t ):
	global isExist, n, A
	isExist[ t ] = True
	if p < n:
		solve( p+1, t-A[p] )
		solve( p+1, t )
	else:
		return

isExist = [False]*2001 
n = int( raw_input() )
A = map( int, raw_input().rstrip().split( " " ) )
q = int( raw_input() )
M = map( int, raw_input().rstrip().split( " " ) )
s = sum( A )
solve( 0, s )
for i in range( 0, q ):
	if isExist[ M[i] ]:
		print( "yes" )
	else:
		print( "no" )