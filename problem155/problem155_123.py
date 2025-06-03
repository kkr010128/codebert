n,m = map(int,input().split())
h = list(map(int,input().split()))

# 隣接リスト
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)  # 有向グラフなら消す

def dfs(x):
    if len(graph[x]) == 0:
        return True
    for i in range(len(graph[x])):
        if h[graph[x][i]] >= h[x]:
            return False
    return True

ans = 0
for i in range(n):
    if dfs(i):
        ans += 1
print(ans)