def input2():
	return map(int,input().split())

#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))

class UnionFind():
	"""docstring for UnionFind"""
	def __init__(self, n):
		self.parents = [-1]*n

	def find(self,x):
		if self.parents[x] < 0: #自分が親である時
			return x
		else: #自分が子供である時
			self.parents[x]=self.find(self.parents[x])
			return self.parents[x]

	def union(self,x,y):
		# 各要素の親要素を返す
		x=self.find(x)
		y=self.find(y)

		if x==y:
			return
		if self.parents[x] > self.parents[y]:
			x,y=y,x

		self.parents[x]+=self.parents[y]
		self.parents[y]=x
		# print(self.parents)

		
n,m=input2()
S=[input_array() for _ in range(m)]

uf=UnionFind(n) #uf.parents==[-1]*n

for s in S:
	uf.union(s[0]-1,s[1]-1)
ans=min(uf.parents)

print(-ans)