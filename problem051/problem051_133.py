import sys

while True:
	h, w = [ int( val ) for val in sys.stdin.readline().split( " " ) ]
	if 0 ==h and 0 == w:
		break
	pa = [ "#", "." ]
	d = 0
	ouput = []
	for i in range( h ):
		d = i%2
		for j in range( w ):
			ouput.append( pa[d] )
			d = not d	
		ouput.append( "\n" )	
	print( "".join( ouput ) )