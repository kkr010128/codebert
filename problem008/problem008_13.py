import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001

global current_time
global visited,go_time,back_time
global G


def dfs(node_id):
    global current_time #書かないとローカル変数扱いされる
    go_time[node_id] = current_time
    current_time += 1

    for next_node in G[node_id]:

        if visited[next_node] == True:
            continue
        visited[next_node] = True
        dfs(next_node)

    back_time[node_id] = current_time
    current_time += 1


V = int(input())

G = [[] for i in range(V)]

visited = [False]*V

go_time = [0]*V
back_time = [0]*V

for loop in range(V):
    node_id,num,*tmp_adj = list(map(int,input().split()))
    node_id -= 1
    for i in range(num):
        G[node_id].append(tmp_adj[i]-1)

current_time = 1;

for i in range(V):
    if visited[i] == True:
        continue
    visited[i] = True
    dfs(i)

for i in range(V):
    print("%d %d %d"%(i+1,go_time[i],back_time[i]))





