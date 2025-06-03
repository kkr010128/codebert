n, q = [ int( val ) for val in raw_input( ).split( " " ) ]
ps = [0]*n
t = [0]*n
for i in range( n ):
    ps[i], t[i] = raw_input( ).split( " " )

qsum = 0
while t:
    psi = ps.pop( 0 )
    ti = int( t.pop( 0 ) )
    if ti <= q:
        qsum += ti
        print( "{:s} {:d}".format( psi, qsum ) )        
    else:
        t.append( ti - q )
        ps.append( psi )
        qsum += q