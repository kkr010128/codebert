mod=998244353

class Combination:
	def __init__(self,size):
		self.size = size + 2
		self.fact = [1, 1] + [0] * size
		self.factInv = [1, 1] + [0] * size
		self.inv = [0, 1] + [0] * size
		
		for i in range(2, self.size):
			self.fact[i] = self.fact[i - 1] * i % mod
			self.inv[i] = -self.inv[mod % i] * (mod//i) % mod
			self.factInv[i] = self.factInv[i - 1] * self.inv[i] % mod
			
	def npk(self,n,k):
		if n < k or n < 0 or k < 0:
			return 0
		return self.fact[n] * self.factInv[n - k] % mod
		
	def nck(self,n,k):
		if n < k or n < 0 or k < 0:
			return 0
		return self.fact[n] * (self.factInv[k] * self.factInv[n - k] % mod) % mod
		
	def nhk(self,n,k):
		return self.nck(n + k - 1, n - 1)


n,m,k=map(int,input().split())

comb=Combination(n+k)
res=0

for i in range(k+1):
	res+=((comb.nhk(n-i,i))*m)%mod*(pow(m-1,n-1-i,mod))
	res%=mod
print(res)