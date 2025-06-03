class Dice():
	def __init__(self, label):
		self.d = label
	
	def roll(self, drt):
		if drt == 'N':
			self.d[1], self.d[2], self.d[6], self.d[5] = self.d[2], self.d[6], self.d[5], self.d[1]
		elif drt == 'E':
			self.d[1], self.d[3], self.d[6], self.d[4] = self.d[4], self.d[1], self.d[3], self.d[6]
		elif drt == 'S':
			self.d[2], self.d[6], self.d[5], self.d[1] = self.d[1], self.d[2], self.d[6], self.d[5]
		elif drt == 'W':
			self.d[4], self.d[1], self.d[3], self.d[6] = self.d[1], self.d[3], self.d[6], self.d[4]
	def printl(self, lct):
		print(self.d[lct])
		
label = [0]	
label.extend(list(map(int, input().split())))
dice1 = Dice(label)
direction = input()
leng = len(direction)

for i in range(leng):
	dice1.roll(direction[i])

dice1.printl(1)