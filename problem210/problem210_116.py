n = int(input())
stmp = list(input())
Q = int(input())
target = ord("a")
s = [ord(stmp[i])-target for i in range(n)]

class BIT:
	"""
	<Attention> 0-indexed.
	query ... return the sum [0 to m]
	sum ... return the sum [a to b]
	sumall ... return the sum [all]
	add ... 'add' number to element (be careful that it doesn't set a value.)
	search ... the sum version of bisect.right
	output ... return the n-th element
	listout ... return the BIT list
	"""
	
	def query(self, m):
		res = 0
		while m > 0:
			res += self.bit[m]
			m -= m&(-m)
		return res
	
	def sum(self, a, b):
		return self.query(b)-self.query(a)
	
	def sumall(self):
		bitlen = self.bitlen-1
		return self.query(bitlen)
	
	def add(self, m, x):
		m += 1
		bitlen = len(self.bit)
		while m <= bitlen-1:
			self.bit[m] += x
			m += m&(-m)
		return
	
	def __init__(self, n):
		self.bitlen = n+1
		self.bit = [0]*(n+1)

b = [BIT(n) for i in range(26)]
for i in range(n):
	b[s[i]].add(i, 1)

for _ in range(Q):
	q,qtmpa,qtmpb = input().split()
	if q[0] == "1":
		qa = int(qtmpa)
		t = ord(qtmpb)-target
		b[t].add(qa-1, 1)
		b[s[qa-1]].add(qa-1, -1)
		s[qa-1] = t
	else:
		ans = 0
		qta = int(qtmpa)
		qtb = int(qtmpb)
		for i in range(26):
			if b[i].sum(qta-1, qtb) != 0:
				ans += 1
		print(ans)
