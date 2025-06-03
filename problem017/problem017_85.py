def insertionSort( nums, n, g ):
	cnt = 0
	for i in range( g, len( nums ) ):
	    v = nums[i]
	    j = i - g
	    while 0 <= j and v < nums[j]:
	        nums[ j+g ] = nums[j]
	        j -= g
	        cnt += 1
	    nums[ j+g ] = v
	
	return cnt


def shellSort( nums, n ):
	cnt = 0
	g = []
	val =0
	for i in range( 0, n ):
		val = 3*val+1
		if  n < val:
			break
		g.append( val )

	g.reverse( )
	m = len( g )
	print( m )
	print( " ".join( map( str, g ) ) )
	for i in range( 0, m ):
		cnt += insertionSort( nums, n, g[i] )
	print( cnt )

n = int( raw_input( ) )
nums = []
for i in range( 0, n ):
	nums.append( int( raw_input( ) ) )

shellSort( nums, n )
for i in nums:
	print( i )