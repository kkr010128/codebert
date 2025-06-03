import sys
 
chash = {}
for i in range( ord( 'a' ), ord( 'z' )+1 ):
    chash[ chr( i ) ] = 0
 
while True:
    line = sys.stdin.readline().rstrip()
    if not line:
        break
    for i in range( len( line ) ):
        if line[i].isalpha():
            chash[ line[i].lower() ] += 1
 
for i in range( ord( 'a' ), ord( 'z' )+1 ):
    print( "{:s} : {:d}".format( chr( i ), chash[ chr( i ) ] ) )