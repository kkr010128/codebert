import sys
import itertools
# import numpy as np
import time
import math
import heapq
 
sys.setrecursionlimit(10 ** 7)
 
from collections import defaultdict
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
# list(map(int, input().split()))

n = int(input())

adj = [[] for i in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    u = line[0]
    for j in range(line[1]):
        v = line[2 + j]
        adj[u - 1].append(v - 1)


# BFS
import queue
q = queue.Queue()
visited = [False] * n
dist = [-1] * n

visited[0] = True
dist[0] = 0
q.put(0)
while not q.empty():
    v = q.get()
    for u in adj[v]:
        if visited[u]:
            continue
        visited[u] = True
        dist[u] = dist[v] + 1
        q.put(u)

for i in range(n):
    val = dist[i]
    print(i + 1, val)
