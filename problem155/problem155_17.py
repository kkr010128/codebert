n,m = map(int,input().split())
graph = [[] for _ in range(n)]
h = list(map(int,input().split()))
for _ in range(m):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
cnt = 0
for i in range(n):
    if graph[i] == []:
        cnt += 1
        continue
    if max([h[j] for j in graph[i]]) < h[i] : cnt += 1
print(cnt)