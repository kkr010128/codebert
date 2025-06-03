import sys
 
chash = {}
for i in range( ord( 'a' ), ord( 'z' )+1 ):
    chash[ chr( i ) ] = 0
 
for line in sys.stdin:
    for i in range( len( line ) ):
        if line[i].isalpha():
            chash[ line[i].lower() ] += 1
 
for i in range( ord( 'a' ), ord( 'z' )+1 ):
    print( "{:s} : {:d}".format( chr( i ), chash[ chr( i ) ] ) )