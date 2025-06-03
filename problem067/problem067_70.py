import sys

tscore = hscore = 0
n = int( sys.stdin.readline() )
for i in range( n ):
	tcard, hcard = sys.stdin.readline().rstrip().split( " " )
	if tcard < hcard:
		hscore += 3
	elif hcard < tcard:
		tscore += 3
	else:
		hscore += 1
		tscore += 1

print( "{:d} {:d}".format( tscore, hscore ) )