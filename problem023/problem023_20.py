n = int( raw_input( ) )
dic = {}
for i in range( n ):
	cmd, word = raw_input( ).split( " " )
	if "insert" == cmd:
		dic[ word ] = True
	elif "find" == cmd:
		if not dic.get( word ):
			print( "no" )
		else:
			print( "yes" )