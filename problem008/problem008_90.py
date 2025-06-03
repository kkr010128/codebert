N = int(input())
edge = [[0] for _ in range(N)]
for i in range(N):
    A = list(map(int, input().split()))
    for i,a in enumerate(A):
        A[i] -= 1
    edge[A[0]] = sorted(A[2:])
ans = [[0,0] for _ in range(N)]
import sys
sys.setrecursionlimit(10**8)

def dfs(v,now):
    if len(edge[v])>0:
        for u in edge[v]:
            if visited[u]==False:
                visited[u]=True
                now += 1
                ans[u][0] = now
                now = dfs(u,now)
    now += 1
    ans[v][1] = now
    return now

visited = [False]*N

now = 0
for i in range(N):
    if visited[i]==False:
        visited[i]=True
        now += 1
        ans[i][0] = now
        now = dfs(i,now)
for i in range(N):
    ans[i] = '{} {} {}'.format(i+1,ans[i][0],ans[i][1])
print(*ans,sep='\n')
