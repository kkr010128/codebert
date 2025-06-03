class uf():


    def __init__(self,n):
        self.size=n
        self.parents=list(range(n))


    def find(self,x):
        if self.parents[x]==x:
            return x
        self.parents[x]=self.find(self.parents[x])
        return self.find(self.parents[x])


    def union(self,a,b):
        x=self.find(a)
        y=self.find(b)
        if x==y:
            return
        if x>y:
            x,y=y,x
        self.parents[y]=x


    def roots(self):
        s=0
        for c in range(self.size):
            if self.find(c)==c:
                s+=1
        return s-1


n,m=map(int,input().split())
city=uf(n)
for c in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    city.union(a,b)
print(city.roots())