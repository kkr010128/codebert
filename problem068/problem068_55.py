s = list( raw_input( ) )
n = int( raw_input( ) )
for i in range( n ):
	cmd = raw_input( ).split( " " )
	a = int( cmd[1] )
	b = int( cmd[2] ) + 1
	if "print" == cmd[0]:
		print( "".join( s[ a:b ] ) )
	elif "reverse" == cmd[0]:
		for i in reversed( s[ a:b ] ):
			s[ a ] = i
			a += 1
	elif "replace" == cmd[0]:
		for i in cmd[3]:
			s[ a ] = i
			a += 1