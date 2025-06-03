N,M=map(int,input().split())

class UnionFind():
    def __init__(self,n): #n:要素数
        self.n=n
        self.parents = [-1]*n 
        #parents:各要素の親要素番号を格納
        #要素が根である場合、-(そのグループの要素数)を格納する
    
    def find(self,x): #xが属する根を返す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]
    
    def union(self,x,y): #xのグループとyのグループを併合する
        x = self.find(x)
        y = self.find(y)
        
        if x==y:
            return
        
        if self.parents[x] > self.parents[y]: #|xのグループ|<|yのグループ|
            x,y=y,x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        #よりグループ数が多い方の根にもう一方のグループを接続
        
    def size(self,x): #xの属するグループのサイズ
        return -self.parents[self.find(x)]

uf=UnionFind(N)
for i in range(M):
    a,b=map(lambda x:int(x)-1,input().split())
    uf.union(a,b)

ans=0

for i in range(N):
    if uf.size(i) > ans:
        ans=uf.size(i)
        
print(ans)