
class Dice:
	
	def __init__(self, faces):
		self.t = faces[0]
		self.s = faces[1]
		self.e = faces[2]
		self.w = faces[3]
		self.n = faces[4]
		self.b = faces[5]

	def roll(self, drct):
		t_ = self.t
		s_ = self.s
		e_ = self.e
		w_ = self.w
		n_ = self.n
		b_ = self.b
		if drct == 'S':
			self.t = n_
			self.s = t_
			self.n = b_
			self.b = s_
		elif drct == 'N':
			self.t = s_
			self.s = b_
			self.n = t_
			self.b = n_
		elif drct == 'E':
			self.t = w_
			self.e = t_
			self.w = b_
			self.b = e_
		elif drct == 'W':
			self.t = e_
			self.e = b_
			self.w = t_
			self.b = w_
		else:
			return
	
	def set_top(self, face):
		if self.t == face:
			return
		elif self.s == face:
			self.roll('N')
		elif self.e == face:
			self.roll('W')
		elif self.w == face:
			self.roll('E')
		elif self.n == face:
			self.roll('S')
		else:
			self.roll('N')
			self.roll('N')
			
	def get_right_face(self, f):
		if self.s == f:
			return self.e
		elif self.e == f:
			return self.n
		elif self.w == f:
			return self.s
		else:
			return self.w
	
faces = list(map(int, input().split()))
dice = Dice(faces)

n = int(input())
for i in range(n):
	t, f = map(int, input().split())
	dice.set_top(t)
	print(dice.get_right_face(f))

