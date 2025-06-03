d=list(map(int,input().split()))
q=int(input())

class dice(object):
	def __init__(self, d):
		self.d = d

	def roll(self,com):
		a1,a2,a3,a4,a5,a6=self.d
		if com=="E":
			self.d = [a4,a2,a1,a6,a5,a3]
		elif com=="W":
			self.d = [a3,a2,a6,a1,a5,a4]
		elif com=="S":
			self.d = [a5,a1,a3,a4,a6,a2]
		elif com=="N":
			self.d = [a2,a6,a3,a4,a1,a5]

dice1=dice(d)
l=[]
for i in range(q):
	l.append(list(map(int,input().split())))

c=["E","W","S","N"]
import random
for i in l:
	while 1:
		if dice1.d[0]==i[0] and dice1.d[1]==i[1]:
			break 
		else:
			dice1.roll(c[random.randint(1,2)])
	print(dice1.d[2])