n = int( raw_input( ) )
dic = {}
output = []
for i in range( n ):
	cmd, word = raw_input( ).split( " " )
	if "insert" == cmd:
		dic[ word ] = True
	elif "find" == cmd:
		if not dic.get( word ):
			output.append( "no" )
		else:
			output.append( "yes" )

print( "\n".join( output ) )