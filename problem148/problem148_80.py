A, B, C, K = map( int, input().split())
ret = min( A, K )
if A < K:
  ret -= max( 0, K - A - B )
print( ret )