class Dice:
	def __init__(self, ls):
		self.ls = ls
		self.now = 0
	
	def roll(self, direction):
		if direction == 'E': pat = [5, 2, 0, 3]
		elif direction == 'N': pat = [5, 4, 0, 1]
		elif direction == 'W': pat = [5, 3, 0, 2]
		elif direction == 'S': pat = [5, 1, 0, 4]

		tmp = self.ls[pat[0]]
		for i in range(4):
			try:
				self.ls[pat[i]] = self.ls[pat[i+1]]
			except(IndexError):
				pass
		self.ls[pat[-1]] = tmp
		
	def top(self):
		return self.ls[self.now]

dice = Dice(list(input().rstrip().split()))
for cmd in list(input().rstrip()):
	dice.roll(cmd)
print(dice.top())
