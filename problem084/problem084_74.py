import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy
INF = 10**9


"""
UnionFind
要素を素集合(互いに素)に分割して管理するデータ構造
O(α)<O(log)
逆アッカーマン関数
"""

class UnionFind():

    def __init__(self,n):
        self.n = n
        self.parents = [-1]*n #各要素の親要素の番号を格納するリスト
    
    #要素xが属するグループの根を返す
    def find(self,x):
        if self.parents[x]<0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    #要素xと要素yが属するグループを併合する   
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        
        if self.parents[x]>self.parents[y]:
            x,y = y,x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    #要素xが属するグループのサイズを返す
    def size(self,x):
        return -self.parents[self.find(x)]
    
    #要素x,yが同じグループかどうかを返す
    def same(self,x,y):
        return self.find(x) == self.find(y)
    
    #要素xと同じグループのメンバーを返す
    def members(self,x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    #すべての根の要素を返す
    def roots(self):
        return [i for i,x in enumerate(self.parents) if x<0]
    
    #グループの数を返す
    def group_count(self):
        return len(self.roots())
    
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    
    def __str__(self):
        return "\n".join("{}: {}".format(r,self.members(r)) for r in self.roots())


if __name__ == "__main__":
    n,m = map(int,input().split())
    uf = UnionFind(n)
    for i in range(m):
        a,b = map(int,input().split())
        a-=1
        b-=1
        uf.union(a,b)
    ans = 0
    for i in range(n):
        c = uf.size(i)
        ans = max(ans,c)
    print(ans)