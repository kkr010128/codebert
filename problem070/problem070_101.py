class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n+1)]  # �?要�?の親要�?の番号を�?�納するリス�?
        self.rank = [0] * (n+1)
        self.size = [1] * (n+1)  # 根?��ルート）�?�場合、そのグループ�?�要�?数を�?�納するリス�?

    # 要�? x が属するグループ�?�根を返す
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 要�? x が属するグループと要�? y が属するグループとを併合す�?
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 要�? x, y が同じグループに属するかど�?かを返す
    def same_check(self, x, y):
        return self.find(x) == self.find(y)
    
    # 要�? x が属するグループに属する要�?をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(1,self.n+1) if self.find(i) == root]

    # 要�? x が属するグループ�?�サイズ?��要�?数?��を返す
    def get_size(self, x):
        return self.size[self.find(x)]

    # すべての根の要�?をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.par) if x == i and i != 0]
    
    # グループ�?�数を返す
    def group_count(self):
        return len(self.roots())
    
    # {ルート要�?: [そ�?�グループに含まれる要�?のリス�?], ...} の辞書を返す
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

n,m = map(int,input().split())
uf = UnionFind(n)
for i in range(m):
    a,b = map(int,input().split())
    uf.union(a,b)
print(len(uf.roots())-1)