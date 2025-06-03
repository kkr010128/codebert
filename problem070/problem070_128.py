import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

class UnionFindPathCompression():
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [1]*n
        self.size = [1]*n
        

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return
        else:
            if self.rank[px] < self.rank[py]:
                self.parents[px] = py
                self.size[py] += self.size[px]
            else:
                self.parents[py] = px
                self.size[px] += self.size[py]
                #ランクの更新
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1


N,M = map(int,input().split())
ufpc = UnionFindPathCompression(N)
for i in range(M):
    a,b = map(int,input().split())
    ufpc.union(a-1,b-1)

ans = 0
for i in range(N-1):
    if ufpc.find(i) != ufpc.find(i+1):
        ufpc.union(i,i+1)
        ans += 1
print(ans)