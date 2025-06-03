from __future__ import print_function
import sys

officalhouse = [0]*4*3*10

n = int( sys.stdin.readline() )
for i in range( n ):
	b, f, r, v = [ int( val ) for val in sys.stdin.readline().split( " " ) ]
	bfr = (b-1)*30+(f-1)*10+(r-1)
	officalhouse[bfr] = officalhouse[bfr] + v;
	
output = []
for b in range( 4 ):
	for f in range( 3 ):
		for r in range( 10 ):
			output.append( " {:d}".format( officalhouse[ b*30 + f*10 + r ] ) )
		output.append( "\n" )
	if b < 3:
		output.append( "####################\n" )

print( "".join( output ), end="" )