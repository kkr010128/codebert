#!/usr/bin/env python3
from networkx.utils import UnionFind
import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    n,m=map(int, input().split())
    uf = UnionFind()
    for i in range(1,n+1):
        _=uf[i]
    for _ in range(m):
        a,b=map(int, input().split())
        uf.union(a, b)  # aとbをマージ
    print(len(list(uf.to_sets()))-1)
    #for group in uf.to_sets():  # すべてのグループのリストを返す
        #print(group)

if __name__ == '__main__':
    main()

