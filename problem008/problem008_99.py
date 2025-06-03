import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy
time = 1
def dfs(node):
    global time
    if visited[node] != -1:
        return
    visited[node] = 0
    d[node] = time
    time += 1
    for v in edge[node]:
        dfs(v)
    f[node] = time
    time += 1

if __name__ == "__main__":
    n = int(input())
    edge = []
    for i in range(n):
        u,k,*v_li = map(int,input().split())
        for j in range(len(v_li)):
            v_li[j] -= 1
        u-=1
        edge.append(v_li)
    d = {}
    f = {}
    visited = [-1]*n
    
    for i in range(n):
        dfs(i)
    for i in range(n):
        print(i+1,d[i],f[i])


