diceface = { "TOP":0,"FRONT":1,"RIGHT":2,"LEFT":3,"BACK":4,"BOTTOM":5 }

dice = [ int( i ) for i in raw_input( ).split( " " ) ]
roll = raw_input( )
for i in range( len(  roll ) ):
	if "E" == roll[i]:
		t = dice[ diceface["TOP"] ]
		dice[ diceface["TOP"] ] = dice[ diceface["LEFT"] ]
		dice[ diceface["LEFT"] ] = dice[ diceface["BOTTOM"] ]
		dice[ diceface["BOTTOM"] ] = dice[ diceface["RIGHT"] ]
		dice[ diceface["RIGHT"] ] = t
	elif "N" == roll[i]:
		t = dice[ diceface["TOP"] ]
		dice[ diceface["TOP"] ] = dice[ diceface["FRONT"] ]
		dice[ diceface["FRONT"] ] = dice[ diceface["BOTTOM"] ]
		dice[ diceface["BOTTOM"] ] = dice[ diceface["BACK"] ]
		dice[ diceface["BACK"] ] = t
	elif "S" == roll[i]:
		t = dice[ diceface["TOP"] ]
		dice[ diceface["TOP"] ] = dice[ diceface["BACK"] ]
		dice[ diceface["BACK"] ] = dice[ diceface["BOTTOM"] ]
		dice[ diceface["BOTTOM"] ] = dice[ diceface["FRONT"] ]
		dice[ diceface["FRONT"] ] = t
	elif "W" == roll[i]:
		t = dice[ diceface["TOP"] ]
		dice[ diceface["TOP"] ] = dice[ diceface["RIGHT"] ]
		dice[ diceface["RIGHT"] ] = dice[ diceface["BOTTOM"] ]
		dice[ diceface["BOTTOM"] ] = dice[ diceface["LEFT"] ]
		dice[ diceface["LEFT"] ] = t	

print( dice[ diceface["TOP"] ] )