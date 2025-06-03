import bisect,collections,copy,heapq,itertools,math,string
from collections import defaultdict as D
from functools import reduce
import numpy as np
import sys
import os
from operator import mul

sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int,LS()))

if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]+'.txt'
    sys.stdin = open(inputFile, "r")

# k: number of transfer
_,k = LI()
a = LI()
# 街の番号を0始まりに変更
a = list(map(lambda x:x-1,a))
# print(a)

s = set([0])

# 再帰関数
def rec(visited,next):
    if next in s:
        # print(visited)
        return visited,visited.index(next)
    else:
        s.add(next)
        visited.append(next)
        return rec(visited,a[next])

visited = [0]
# 訪れた街、初めて2度訪れた街のインデックスを取得
visited,loopStart = rec(visited,a[0])

# print(visited,loopStart)

if k < len(visited):
    townIndex = visited[k]
else:
    visitedLoop = visited[loopStart:]
    # print(visitedLoop)
    # 残り回数を循環配列の長さで割った余り
    index = (k-(loopStart))%len(visitedLoop)
    # print(index)
    townIndex = visitedLoop[index]

print(townIndex+1)