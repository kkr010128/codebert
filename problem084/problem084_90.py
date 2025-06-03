from sys import stdin
inp = lambda : stdin.readline().strip()


def dfs_iter(n):
    stack = [n]
    ans = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            ans += 1
            for child in adj[node]:
                if not visited[child]:
                    stack.append(child)
    return ans

n, m = [int(x) for x in inp().split()]
adj = [set() for i in range(n)]
visited = [False]*n
for i in range(m):
    u, v = [int(x) for x in inp().split()]
    adj[u - 1].add(v - 1)
    adj[v - 1].add(u - 1)
ans = 0
for i in range(n):
    if not visited[i]:
        ans = max(ans, dfs_iter(i))
print(ans)