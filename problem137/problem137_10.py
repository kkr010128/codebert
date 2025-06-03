n = int( input() )
A = []
B = []
for i in range(n):
  a, b = map( int, input().split() )
  A.append( a )
  B.append( b )
A = sorted( A )
B = sorted( B )

ret = 0
if n % 2 == 0:
  i = n // 2 - 1
  ret = B[ i + 1 ] + B[ i ] - ( A[ i + 1 ] + A[ i ] ) + 1
else:
  i = ( n + 1 ) // 2 - 1
  ret = B[ i ] - A[ i ] + 1
  
print( ret )