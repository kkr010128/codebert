N = int( input( ) )
x = N % 1000
if x == 0 :
    print( '0' )
else :
    print( 1000 - int(x) )