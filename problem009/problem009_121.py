N = int(input())
edge = [[] for _ in range(N)]

for _ in range(N):
    l = list(map(int, input().split()))
    for j in range(l[1]):
        edge[l[0]-1].append(l[2+j]-1)


now_list = [0]
next_list = []
dist = 0
dists = [-1] * N
while len(now_list) > 0:
    for _ in range(len(now_list)):
        v = now_list.pop()
        if dists[v] == -1:
            dists[v] = dist
        else:
            continue
        for nv in edge[v]:
            next_list.append(nv)
    now_list = next_list
    next_list = []
    dist += 1

for i in range(N):
    print(1+i, dists[i])

