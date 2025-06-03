class UnionFind:
    def __init__(self,n):
        self.par = [-1] * n     # 負数は友達の数（自分を含む）初期値は自分-1、0と正数は根を示す

    def root(self,x):   # xの根を返す
        if self.par[x] < 0:    # xが根の時は、xを返す
            return x
        self.par[x] = self.root(self.par[x])    # 根でないときは、par[x]に根の根を代入
        return self.par[x]                      # 根の根を返す

    def union(self,x,y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.par[x] > self.par[y]:     # par[x]が小さく(友達が多く)なるように交換
            x, y = y, x
        self.par[x] += self.par[y]  # 友達が多い方に少ない方を加える
        self.par[y] = x             # yの根をxにする

    def size(self):
        return -1 * min(self.par)


n, m = map(int, input().split())
uf = UnionFind(n)

for _ in range(m):
    a, b = map(int, input().split())
    uf.union(a-1,b-1)               # 1が0番目、２が1番目・・・

print(uf.size())