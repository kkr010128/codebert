#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
import heapq
#from fractions  import gcd
#input=sys.stdin.readline
import bisect
n,m=map(int,input().split())
class UnionFind(): #集合の取り扱い、辺に重み、階層を意識するときは使えない
    def __init__(self,n):
        self.n=n
        self.par = [-1]*n
    def find(self,x):
        if self.par[x] <0: #負なら親、要素数
            return x
        else: #正なら親の番号
            self.par[x]=self.find(self.par[x]) #一回調べたら根を繋ぎ変える、経路圧縮
            return self.par[x]
    def union(self,x,y):
        x=self.find(x) #x,yの親
        y=self.find(y)

        if x==y: #親が同じなら何もしない
            return 
        if self.par[x]>self.par[y]: #要素数が大きい方をxにする
            x,y=y,x
        self.par[x]+=self.par[y] #xがある集合にyが入った集合をくっつける
        self.par[y]=x

    def size(self,x):
        return -self.par[self.find(x)] #親のサイズ
    
    def same(self,x,y): #親が同じ、すなわち同じ集合か
        return self.find(x)==self.find(y)

    def member(self,x): #同じ木（集合）にある要素全部リストで返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i)==root ]
    
    def roots(self): #集合の根になってる要素をリストで返す
        return [i for i , x in enumerate(self.par) if x<0]
    
    def group_count(self): #集合の数、木の数
        return len(self.roots())

    def all_member(self): #辞書型で返す
        return {r: self.member(r) for r in self.roots()}
    def __str__(self):
        return "\n".join('{}:{}'.format(r,self.member(r)) for r in self.roots)

tree=UnionFind(n)
for i in range(m):
    a,b=map(int,input().split())
    tree.union(a-1,b-1)
print(tree.group_count()-1)