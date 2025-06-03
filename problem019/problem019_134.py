from Queue import Queue

n, q = [ int( val ) for val in raw_input( ).split( " " ) ]
names = Queue( )
times = Queue( )
for i in range( n ):
	name, time = raw_input( ).split( " " )
	names.put( name )
	times.put( int( time ) )
 
qsum = 0
output = []
while not times.empty( ):
	name = names.get( )
	time = times.get( )
	if time <= q:
		qsum += time
		output.append( "{:s} {:d}".format( name, qsum ) )
	else:
		times.put( time - q )
		names.put( name )
		qsum += q

print( "\n".join( output ) )