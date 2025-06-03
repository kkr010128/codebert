n = int(input())

adj_list = [[] for _ in range(n + 1)]

for i in range(n):
    tmp = list(map(int, input().split()))
    u = tmp[0]
    k = tmp[1]
    for v in range(2, 2 + k):
        adj_list[u].append(tmp[v])

d = [-1] * (n + 1)
q = []
q.append(1)
d[1] = 0

while len(q) > 0:
    u = q.pop(0)
    for v in adj_list[u]:
        if d[v] == -1:
            d[v] = d[u] + 1
            q.append(v)

for idx, d in enumerate(d):
    if idx != 0:
        print("%d %d" % (idx, d))


