class UnionFind():
    def __init__(self,n):
        self.n=n
        self.root=[-1]*n
        self.rank=[-1]*n

    def Find_Root(self,x):
        if self.root[x]<0:return x
        else:
            self.root[x]=self.Find_Root(self.root[x])
            return self.root[x]

    def Unite(self,x,y):
        x=self.Find_Root(x)
        y=self.Find_Root(y)

        if x==y:return
        elif self.rank[x]>self.rank[y]:
            self.root[x] +=self.root[y]
            self.root[y]=x
        else:
            self.root[y] +=self.root[x]
            self.root[x]=y
            if self.rank[x]==self.rank[y]:
                self.rank[y] +=1

    def isSameGroup(self,x,y):
        return self.Find_Root(x)==self.Find_Root(y)

    def size(self,x):
        return -self.root[self.Find_Root(x)]

    def members(self,x):
        root=self.Find_Root(x)
        return [i for i in range(self.n) if self.Find_Root(i)==root]

    def roots(self):
        return[i for i,j in enumerate(self.root) if j<0]

    def group_members(self):
        return {i:self.members(i) for i in self.roots()}

    def group_count(self):
        return len(self.roots())


N,K=map(int,input().split())
P=list(map(int,input().split()))
C=list(map(int,input().split()))

UnionFind=UnionFind(N+1)
for i in range(N):
    UnionFind.Unite(i+1,P[i])

D=UnionFind.group_members()
E=[]
for i in D:
    A,length=D[i],len(D[i])
    if A[0]==0:continue
    index,F=A[0]-1,[]
    while len(F)!=length:
        index=P[index]-1
        F.append(C[index])
    E.append(F)

ans=-float("inf")
for A in E:
    length=len(A)
    if sum(A)<0:
        A=A*2
        for i in range(length):
            point=0
            for j in range(min(K,length)):
                point +=A[i+j]
                ans=max(ans,point)
    else:
        div,mod=divmod(K,length)
        base=(div-1)*sum(A)
        A=A*3
        for i in range(length):
            point=0
            for j in range(mod+length):
                point +=A[i+j]
                ans=max(ans,base+point)
print(ans)