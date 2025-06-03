class Dice:	
	def __init__( self, nums ):
		self.face = nums
	
	def rolltoTop( self, dicenum ):	
		num = 0
		for i,val in enumerate( self.face ):
			if dicenum == val:
				num = i
				break
		if num == 1:
			self.roll( "N" )
		elif num == 2:
			self.roll( "W" )
		elif num == 3:
			self.roll( "E" )
		elif num == 4:
			self.roll( "S" )
		elif num == 5:
			self.roll( "NN" )
	
	def roll( self, actions ):
		for act in actions:
			t = 0
			if act == "E":
				t =   self.face[0]
				self.face[0] =   self.face[3]
				self.face[3] =   self.face[5]
				self.face[5] =   self.face[2]
				self.face[2] = t
			elif  act == "N":
				t =   self.face[0]
				self.face[0] =   self.face[1]
				self.face[1] =   self.face[5]
				self.face[5] =   self.face[4]
				self.face[4] = t
			elif  act == "S":
				t =  self.face[ 0]
				self.face[0] =  self.face[4]
				self.face[4] =  self.face[5]
				self.face[5] =  self.face[1]
				self.face[1] = t	
			elif  act == "W":
				t =  self.face[0]
				self.face[0] =  self.face[2]
				self.face[2] =  self.face[5]
				self.face[5] =  self.face[3]
				self.face[3] = t	
			elif  act == "M":
				t =  self.face[1]
				self.face[1] =  self.face[2]
				self.face[2] =  self.face[4]
				self.face[4] =  self.face[3]
				self.face[3] = t

diceface = [ int( val ) for val in raw_input( ).split( " " ) ]
dice = Dice( diceface )
q = int( raw_input( ) )
for i in range( q ):
	topnum, frontnum = [ int( val ) for val in raw_input( ).split( " " ) ]
	dice.rolltoTop( topnum )
	while dice.face[1] != frontnum:
		dice.roll( "M" )
		
	print( dice.face[2] )