from collections import defaultdict

def dfs(here, connect, visited, answer):
    global time
    answer[here][1] = time
    time += 1
    visited[here] = 1
    for c in connect[here]:
        if not visited[c]:
            dfs(c, connect, visited, answer)
    answer[here][2] = time
    time += 1

v_num = int(input())
connect = defaultdict(list)
for _ in range(v_num):
    inp = [int(n) - 1 for n in input().split(" ")]
    connect[inp[0]].extend(sorted(inp[2:]))
answer = [[n + 1 for m in range(3)] for n in range(v_num)]
time = 1
visited = [0 for n in range(v_num)]
for i in range(v_num):
    if not visited[i]:
        dfs(i, connect, visited, answer)
for v in range(v_num):
    print(*answer[v])