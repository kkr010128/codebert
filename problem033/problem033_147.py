class Dice(object):
	def __init__(self,List):
		self.face=List
	
	def n_spin(self,List):
		temp=List[0]
		List[0]=List[1]
		List[1]=List[5]
		List[5]=List[4]
		List[4]=temp

	def s_spin(self,List):
		temp=List[0]
		List[0]=List[4]
		List[4]=List[5]
		List[5]=List[1]
		List[1]=temp

	def e_spin(self,List):
		temp=List[0]
		List[0]=List[3]
		List[3]=List[5]
		List[5]=List[2]
		List[2]=temp

	def w_spin(self,List):
		temp=List[0]
		List[0]=List[2]
		List[2]=List[5]
		List[5]=List[3]
		List[3]=temp

dice = Dice(map(int,raw_input().split()))
command = list(raw_input())
for k in command:
	if k=='N':
		dice.n_spin(dice.face)
	elif k=='S':
		dice.s_spin(dice.face)
	elif k=='E':
		dice.e_spin(dice.face)
	else:
		dice.w_spin(dice.face)
print dice.face[0]