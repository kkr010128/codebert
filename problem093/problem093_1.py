n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
p.insert(0, 0)
c.insert(0, 0)
visit = [0] * (n + 1)
cyclelist = []
for i in range(1, n + 1):
    if visit[i] == 0:
        a = [c[i]]
        visit[i] = 1
        while visit[p[i]] == 0:
            i = p[i]
            visit[i] = 1
            a.append(c[i])
        cyclelist.append(a)
ans = -1145141919810
for cycle in cyclelist:
    s = sum(cycle)
    l = len(cycle)
    a = 0
    if l < k and s > 0:
        a = s * ((k - 1) // l)
    now = 0
    x = k % l
    if x == 0:
        x = l
    for i in range(min(k, l)):
        now += cycle[i]
        for j in range(l):
            now += cycle[(i + j + 1) % l] - cycle[j]
            if i < x:
                ans = max(ans, a + now)
            else:
                ans = max(ans, now)
print(ans)