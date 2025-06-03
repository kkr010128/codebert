import sys

while True:
	h, w = [ int( val ) for val in sys.stdin.readline().split( " " ) ]
	if 0 ==h and 0 == w:
		break
	for i in range( h ):
		if 0 == i or h-1 == i:
			print( "#"*w )
		else:
			print( "#"+"."*(w -2)+"#"  )
	print( "" )