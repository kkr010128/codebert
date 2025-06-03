n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
done = [False] * n
s = []
cnt = 0
for i in range(n):
    if not done[i]:
        s.append(i)
        while not s == []:
            v = s.pop()
            done[v] = True
            for nxt in edge[v]:
                if not done[nxt]:
                    s.append(nxt)
        cnt += 1
print(cnt - 1)