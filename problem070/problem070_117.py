'''
Created on 2020/09/26

@author: harurun
'''
#UnionFind(要素数)で初期化
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        #parents 各要素の親番号を格納するリストを返す

    #要素xが属するグループを返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    #要素xとyが属するグループを併合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    #要素xが属するグループのサイズ
    def size(self, x):
        return -self.parents[self.find(x)]

    #要素xとyが同じグループに属するかどうか
    def same(self, x, y):
        return self.find(x) == self.find(y)

    #要素xが属するグループを返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    #すべての根の要素
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    #グループの数
    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write

  N,M=map(int,pin().split())
  ans=0
  uf=UnionFind(N)
  for i in range(M):
    A,B=map(int,pin().split())
    uf.union(A-1, B-1)
  print(uf.group_count()-1)
  return 
main()
