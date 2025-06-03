h, n = map( int, input().split() )
a = []
b = []
for _ in range( n ):
    a_i, b_i = map( int, input().split() )
    a.append( a_i )
    b.append( b_i )

dp = [ float( "Inf" ) ] * ( h + 1 )
# dp[ d ] = dを与える最小マナ
dp[ 0 ] = 0
for i in range( h ):
    for j in range( n ):
        update_index = min( i + a[ j ], h )
        dp[ update_index ] = min( dp[ update_index ], dp[ i ] + b[ j ] )

print( dp[ h ] )