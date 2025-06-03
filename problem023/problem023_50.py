n = int( raw_input( ) )
dic = {}
output = []
for i in range( n ):
	cmd, word = raw_input( ).split( " " )
	if "insert" == cmd:
		dic[ word ] = True
	elif "find" == cmd:
		try:
			dic[ word ]
			output.append( "yes" )
		except KeyError:
			output.append( "no" )

print( "\n".join( output ) )