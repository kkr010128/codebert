n = int( input() )
p = tuple( map( int, input().split() ) )
q = tuple( map( int, input().split() ) )

import itertools
permutations = list( itertools.permutations( range( 1, n + 1 ) ) )
p_order = permutations.index( p )
q_order = permutations.index( q )

print( abs( p_order - q_order ) )