def insertionSort( nums, n, g ):
    cnt = 0
    for i in range( g, n ):
        v = nums[i]
        j = i - g
        while j >= 0 and nums[j] > v:
            nums[ j+g ] = nums[j]
            j -= g
            cnt += 1
         
        nums[ j+g ] = v
    return cnt
         
def shellSort( nums, n ):
    g = []
    v = 1
    while v <= n:
        g.append( v )
        v = 3*v+1     
    g.reverse( )
    m = len( g )
    print( m )
    print( " ".join( map( str, g ) ) )  
    cnt = 0
    for i in range( m ):
        cnt += insertionSort( nums, n, g[i] )
    print( cnt )
 
 
n = int( input( ) )
nums = [ int( input( ) ) for i in range( n ) ]
nums.append( 0 )
shellSort( nums, n )
nums.pop( )
for v in nums:
    print( v )