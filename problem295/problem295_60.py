import sys
import copy

N, M, L = list(map(int, sys.stdin.readline().strip().split(" ")))
INF = 10**10

def warshall_floyd(g_mat):
    dp = copy.copy(g_mat)
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
    return dp

graph = [[INF for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a, b, c = list(map(int, sys.stdin.readline().strip().split(" ")))
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c

dist_graph = warshall_floyd(graph)
bool_graph = [[INF for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if dist_graph[i][j] <= L:
            bool_graph[i][j] = 1

ans_graph = warshall_floyd(bool_graph)

Q = int(sys.stdin.readline().strip())
for _ in range(Q):
    s, t = list(map(int, sys.stdin.readline().strip().split(" ")))
    ans = ans_graph[s-1][t-1]
    print(ans-1 if ans != INF else -1)

    
