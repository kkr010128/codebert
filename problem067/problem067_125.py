tscore = hscore = 0
n = int( input( ) )
for i in range( n ):
	tcard, hcard = input( ).split( " " )
	if tcard < hcard:
		hscore += 3
	elif hcard < tcard:
		tscore += 3
	else:
		hscore += 1
		tscore += 1

print( "{:d} {:d}".format( tscore, hscore ) )