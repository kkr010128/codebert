n = int(input())
d = [0]*(n+1)
f = [0]*(n+1)
t = 1

adjacent_list = [[] for _ in range(n+1)]
for i in range(n):
    e = list(map(int,input().split()))
    if e[1] != 0:
        adjacent_list[i+1].extend(e[2:])
#print(adjacent_list)

def dfs(v):
    if d[v] >= 1:
        return

    global t
    if d[v] == 0: #未発見なら発見時刻を記入
        d[v] = t
    t += 1

    for nv in adjacent_list[v]:
        dfs(nv)
    f[v] = t
    t += 1

for v in range(1,n+1):
    dfs(v)

#dfs(1)
#print(d)
#print(f)
for i in range(1,n+1):
    print(i, d[i], f[i])
