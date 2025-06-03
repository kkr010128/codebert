class diceClass:
	def __init__(self, valuelist):
		self.valuelist = valuelist
		self.t = valuelist[0]
		self.b = valuelist[5]
		self.n = valuelist[4]
		self.s = valuelist[1]
		self.e = valuelist[2]
		self.w = valuelist[3]

	def throw(self, direction):
		# N,S,W,E
		if direction == 'N':
			self.t, self.s, self.b, self.n = self.s, self.b, self.n, self.t
		elif direction == 'S':
			self.t, self.s, self.b, self.n = self.n, self.t, self.s, self.b
		elif direction == 'W':
			self.t, self.e, self.b, self.w = self.e, self.b, self.w, self.t
		elif direction == 'E':
			self.t, self.e, self.b, self.w = self.w, self.t, self.e, self.b


arrinput = list(map(int, input().split()))
dirinput = input()
dice = diceClass(arrinput)
for s in dirinput:
	dice.throw(s)
print(dice.t)

