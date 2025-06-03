import sys

while True:
	h, w = [ int( val ) for val in sys.stdin.readline().split( " " ) ]
	if 0 ==h and 0 == w:
		break
	pa = [ "#", "." ]
	ouput = []
	for i in range( h ):
		for j in range( w ):
			ouput.append( pa[(i+j)%2] )	
		ouput.append( "\n" )	
	print( "".join( ouput ) )