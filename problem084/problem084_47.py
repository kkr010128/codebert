
class unionfind():

    def __init__(self,n):
        #親番号<0なら根
        #根の場合、数値の絶対値が要素数
        self.par=[-1 for i in range(n)]
        
    def root(self,x):
        
        par=self.par
        if par[x]<0:
            return x
        else:
            self.x = self.root(par[x])
            return self.x
        
    def unite(self,x,y):
        #高いほうに低いほうをくっつける
        rx=self.root(x)
        ry=self.root(y)
        
        if rx==ry:
            return
        else:
            if self.par[rx]>self.par[ry]:
                rx,ry = ry,rx
                
            self.par[rx]+=self.par[ry]
            self.par[ry] = rx

            
    def same(self, x,y):
        return self.root(x) == self.root(y)
    
    def par_print(self):
        print(self.par)
        
    def count(self, x):
        return -self.root(x)
    
n,m = map(int,input().split())

friend = unionfind(n)

for i in range(m):
    a,b = map(int,input().split())
    friend.unite(a-1,b-1)
    # print(friend.par_print())
    
# print(friend.par_print())

ans = -min(friend.par)

print(ans)