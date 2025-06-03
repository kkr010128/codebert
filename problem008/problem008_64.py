#ALDS_11_B - 深さ優先探索
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)#再帰回数の上限

def DFS(u, cnt):
    visited.add(u)
    first_contact = cnt
    
    cnt += 1
    for nb in edge[u]:
        if nb not in visited:
            cnt = DFS(nb, cnt)
    
    stamp[u] = first_contact, cnt
    return cnt+1
    

N = int(input())
edge = [[] for i in range(N)]
for _ in range(N):
    tmp = list(map(int,input().split()))
    if tmp[1] != 0:
        edge[tmp[0]-1] = list(map(lambda x: int(x-1),tmp[2:]))

stamp = [None]*N
visited = set()

c = 1
for i in range(N):
    if i not in visited:
        c = DFS(i, c)
        
for i,s in enumerate(stamp):
    print(i+1,*s)
