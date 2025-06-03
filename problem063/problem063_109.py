import sys
 
chash = {}
for i in range( ord( 'a' ), ord( 'z' )+1 ):
    chash[ chr( i ) ] = 0

lines = sys.stdin.readlines()
for i in range( len( lines ) ):
	for j in range( len( lines[i] ) ):
	    if lines[i][j].isalpha():
	        chash[ lines[i][j].lower() ] += 1
 
for i in range( ord( 'a' ), ord( 'z' )+1 ):
    print( "{:s} : {:d}".format( chr( i ), chash[ chr( i ) ] ) )	