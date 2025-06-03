n = int(raw_input())



graph = [[] for i in range(n)]
for i in range(n):
    entry = map(int,raw_input().strip().split(' '))
    u = entry[0]-1
    for v in entry[2:]:
        v -= 1
        graph[u].append(v)

d = [-1 for i in range(n)]
d[0] = 0
t = 1
q = []
q.append(0)
while len(q) > 0:
    u = q[0]
    for v in graph[u]:
        if d[v] == -1:
            q.append(v)
            d[v] = d[u]+1
    del q[0]

for i in range(n):
    print i+1,d[i]