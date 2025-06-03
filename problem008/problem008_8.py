N = int(input())

G = [[0] * N for _ in range(N)]
time = 0
times = [{'s': 0, 'f': 0} for _ in range(N)]

for _ in range(N):
    u, n, *K = map(int, input().split())
    for k in K:
        G[u - 1][k - 1] = 1

def dfs(u):
    global time
    time += 1
    times[u]['s'] = time
    for i in range(N):
        if G[u][i] == 1 and times[i]['s'] == 0:
            dfs(i)
    else:
        time += 1
        times[u]['f'] = time

for i in range(N):
    if times[i]['s'] == 0:
        dfs(i)

for i, time in enumerate(times):
    print(i + 1, *time.values())

