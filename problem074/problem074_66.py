#BITを使ってみる
n, k = map(int, input().split())
lr = []
for _ in range(k):
    l, r = map(int, input().split())
    lr.append((l, r))
mod = 998244353
class BinaryIndexedTree():
    def __init__(self, n, mod=None):
        self.n = n
        self.mod = mod
        self.bit = [0]*n
    
    def add(self, i, w):
        x = i+1
        while x<=self.n:
            self.bit[x-1] += w
            if self.mod is not None:
                self.bit[x-1] %= mod
            x += x & -x
    
    def sum(self, l, r):
        return self._sum(r-1) - self._sum(l-1)

    def _sum(self, i):
        ret = 0
        x = i+1
        while x>0:
            ret += self.bit[x-1]
            if self.mod is not None:
                ret %= self.mod
            x -= x & -x
        return ret
bit = BinaryIndexedTree(2*n+1, mod)
bit.add(n+1, 1)
for i in range(n+2, 2*n+1):
    for l, r in lr:
        bit.add(i, bit.sum(i-r, i-l+1))
print(bit.bit[2*n])