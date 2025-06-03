import numpy as np
from sys import stdin

def getval():
    n,m = map(int,input().split())
    path = [[] for i in [0]*(n+1)]
    for i in [0]*m:
        a,b = map(int, stdin.readline().split())
        path[a].append(b)
        path[b].append(a)
    return n,m,path

def solve(n,m,p):
    prev = np.zeros((n+1))
    q = [1]
    while q:
        idx = q.pop(0)
        adj = p[idx]
        for i in adj:
            if prev[i]:
                continue
            prev[i] = idx
            q.append(i)
    print("Yes")
    for i in range(2,n+1):
        print(int(prev[i]))

if __name__=="__main__":
    n,m,p = getval()
    #print(p)
    solve(n,m,p)