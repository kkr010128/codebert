from collections import deque
import sys
input = sys.stdin.readline

def main():
    N,X,Y = map(int,input().split())
    edge = [[] for _ in range(N)]
    for i in range(N):
        if i == 0:
            edge[i].append(i+1)
        elif i == N-1:
            edge[i].append(i-1)
        else:
            edge[i].append(i-1)
            edge[i].append(i+1)
    edge[X-1].append(Y-1)
    edge[Y-1].append(X-1)
    
    ans = [0]*(N-1)
    
    for i in range(N):
        visited = [0]*N
        dist = [0]*N
        q = deque([i])#i番目のノードを根とする探索
        visited[i] = 1
        while q:
            now = q.popleft()
            for connection in edge[now]:
                if visited[connection]:
                    dist[connection] = min(dist[connection],dist[now]+1)
                else:
                    visited[connection] = 1
                    dist[connection] = dist[now] + 1
                    q.append(connection)
        for d in dist:
            if d == 0:
                continue
            ans[d-1] += 1
    ans = list(map(lambda x: x//2,ans))
    print(*ans,sep="\n")
if __name__ == '__main__':
    main()