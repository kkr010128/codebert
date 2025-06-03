n = int( raw_input( ) )
t = [ int( val ) for val in raw_input( ).rstrip( ).split( " " ) ]
q = int( raw_input( ) )
s = [ int( val ) for val in raw_input( ).split( " " ) ]

cnt = 0
for si in s:
	for ti in t:
		if si == ti:
			cnt += 1
			break

print( cnt )