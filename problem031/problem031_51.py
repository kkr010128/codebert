import math

while True:
	n = int( raw_input() )
	if 0 == n:
		break
	s = [ float( i ) for i in raw_input( ).split( " " ) ]
	t = sum( s )
	m = t / n
	t = 0
	for val in s:
		t += ( val - m )**2
	print( math.sqrt( t/n ) )