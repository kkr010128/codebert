#

import sys
input=sys.stdin.readline
from collections import deque

def main():
    N,X,Y=map(int,input().split())
    X-=1
    Y-=1
    adj=[[] for i in range(N)]
    adj[X].append(Y)
    adj[Y].append(X)
    for i in range(N-1):
        adj[i].append(i+1)
        adj[i+1].append(i)
    cnt=[0]*(N)
    for i in range(N):
        dist=[-1]*N
        qu=deque([i])
        dist[i]=0
        while(len(qu)>0):
            v=qu.popleft()
            for nv in adj[v]:
                if dist[nv]==-1:
                    dist[nv]=dist[v]+1
                    cnt[dist[nv]]+=1
                    qu.append(nv)
    for i in range(1,N):
        print(cnt[i]//2)
    
    
if __name__=="__main__":
    main()
