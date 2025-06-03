class UnionFind:
	"""
	class UnionFind
	https://note.nkmk.me/python-union-find/
	
	order O(log(n))
	
	n = the number of elements
	parents = the list that contains "parents" of x. be careful that it doesn't contain "root" of x.
	"""
	def __init__(self, n):
		"""
		make UnionFind
		:param n: the number of elements
		"""
		self.n = n
		self.parents = [-1] * n
	
	def find(self, x):
		"""
		:param x: an element
		:return: the root containing x
		"""
		if self.parents[x] < 0:
			return x
		else:
			self.parents[x] = self.find(self.parents[x])
			return self.parents[x]
	
	def union(self, x, y):
		"""
		:param x, y: an element
		"""
		# root
		x = self.find(x)
		y = self.find(y)
		if x == y:
			# already same group so do nothing
			return
		if self.parents[x] > self.parents[y]:
			# the root should be min of group
			x, y = y, x
		# remind that x, y is the root, x < y, then, y unions to x.
		self.parents[x] += self.parents[y]
		# and then y's parent is x.
		self.parents[y] = x
	def size(self, x):
		# return the size of group
		return -self.parents[self.find(x)]
	
	def same(self, x, y):
		# return whether the x, y are in same group
		return self.find(x) == self.find(y)
	
	def members(self, x):
		# return members of group
		root = self.find(x)
		return [i for i in range(self.n) if self.find(i) == root]
	
	def roots(self):
		# return all roots
		return [i for i, x in enumerate(self.parents) if x < 0]
	
	def group_count(self):
		# return how many groups
		return len(self.roots())
	
	def all_group_members(self):
		# return all members of all groups
		return {r: self.members(r) for r in self.roots()}

n,m= map(int,input().split())
union = UnionFind(n)
for i in range(m):
	a,b = map(int,input().split())
	union.union(a-1,b-1)
print(union.group_count()-1)