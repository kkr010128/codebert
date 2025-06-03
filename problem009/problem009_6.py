from collections import deque

n = int(input())
adj = [[]]
for i in range(n):
    adj.append(list(map(int, input().split()))[2:])

ans = [-1]*(n+1)
ans[1] = 0

q = deque([1])
visited = [False] * (n+1)
visited[1] = True

while q:
    x = q.popleft()
    for y in adj[x]:
        if visited[y] == False:
            q.append(y)
            ans[y] = ans[x]+1
            visited[y] = True

for j in range(1, n+1):
    print(j, ans[j])
