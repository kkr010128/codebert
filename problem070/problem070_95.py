# Connect Cities
# Union Findデータ構造（素集合データ構造）
 
#入力:N,M(int:整数)
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
 

		self.parents[y]=x

n,m=input2()
AB=[input_array() for _ in range(m)]
 
uf = UnionFind(n)
for ab in AB:
	a=ab[0]
	b=ab[1]
	uf.union(a-1,b-1)

ans=0
for i in uf.parents:
	if i < 0:
		ans+=1

print(ans-1)