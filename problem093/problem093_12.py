n , k = map(int, input().split())
p = list(map(int,input().split()))
c = list(map(int,input().split()))

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

uf = UnionFind(n)

for i in range(n):
    uf.union(i,p[i]-1)

ma = float('INF')*(-1)
listcase = []
cc=0
for i in uf.roots():
    st = uf.members(i)[0]
    listcase.append([])
    while True:
        listcase[cc].append(c[st])
        st=p[st]-1
        if st == uf.members(i)[0]:
            break
    cc+=1

for i in listcase:
    m = len(i)
    i2=i*2
    su = 0
    if sum(i)>0:
        su = sum(i)*(k//m)
    m2 = k%m
    if m2==0 and su>0:
        m2=m
        su-=sum(i)
    elif m2==0:
        m2=m
    if sum(i)<=0:
        m2=m
    for l in range(m):
        dp=[float('INF')*(-1)]*(m*2)
        dp[l]=i2[l]
        for j in range(l+1,l+m2):
            dp[j]=max(dp[j-1]+i2[j],i2[j])
        ma = max(ma,su+max(dp))
print(ma)
