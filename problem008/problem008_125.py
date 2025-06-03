# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:19:34 2020

@author: Kanaru Sato
"""
def dfs(v):
    global t
    d[v] = t
    t += 1
    if conlist[v]:
        for connectedv in conlist[v]:
            if d[connectedv] == -1:
                dfs(connectedv)
    f[v] = t
    t += 1

n = int(input())
conlist = [[] for i in range(n)]
for i in range(n):
    _ = list(map(int,input().split()))
    [conlist[i].append(_[k]-1) for k in range(2,_[1]+2)]

d = [-1 for i in range(n)]
f = [-1 for i in range(n)]
t = 1

for i in range(n):
    if d[i] == -1:
        dfs(i)    

for i in range(n):
    print(i+1,d[i],f[i])
