class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)
 
    def to_sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= (i & -i)
        return s
 
    def add(self, i, x):
        while i <= self.n:
            self.data[i] += x
            i += (i & -i)
 
    def get(self, i, j):
        return self.to_sum(j)-self.to_sum(i-1)



N = int(input())
A = list(map(int,input().split()))
A.sort()
M = pow(10,6)+ 100
Tree = BIT(M)
for x in A:
  Tree.add(x,1)
ans = 0
for i in range(N):
  for j in range(i+1,N):
    x = A[i]; y = A[j]
    Tree.add(x,-1);Tree.add(y,-1)
    MIN = abs(x-y)+1; MAX = (x+y)-1
    #print(x,y,MIN,MAX)
    ans += Tree.get(MIN,MAX)
    Tree.add(x,1);Tree.add(y,1)
    #print(ans)
print(ans//3)