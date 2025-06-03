import sys

def insertionSort( nums, n, g ):
	cnt = 0
	i = g
	while i < n:
		v = nums[i]
		j = i - g
		while 0 <= j and v < nums[j]:
			nums[ j+g ] = nums[j]
			j -= g
			cnt += 1
		nums[ j+g ] = v
		i += 1
	return cnt
		
def shellSort( nums, n ):
	g = []
	val =0
	for i in range( n ):
		val = 3*val+1
		if  n < val:
			break
		g.append( val )
	
	g.reverse( )
	m = len( g )
	print( m )
	print( " ".join( map( str, g ) ) )
	cnt = 0
	for i in range( m ):
		cnt += insertionSort( nums, n, g[i] )
	print( cnt )
    
n = int( sys.stdin.readline( ) )
nums = []
for i in range( n ):
	nums.append( int( sys.stdin.readline( ) ) )

cnt = 0
shellSort( nums, n )
print( "\n".join( map( str, nums ) ) )