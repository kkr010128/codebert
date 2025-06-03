from collections import defaultdict

def dfs(edges, n, d, f, time):
    if n in d:
        return
    time[0] += 1
    d[n] = time[0]
    for to in edges[n]:
        dfs(edges, to, d, f, time)
    time[0] += 1
    f[n] = time[0]

N = int(input())

edges = defaultdict(list)

for _ in range(N):
    l = list(map(int, input().split()))
    fr = l[0]
    degree = l[1]
    edges[fr] = l[2:]

d = {} # discover time                                                                                                                                                                                      
f = {} # finish time                                                                                                                                                                                        

time = [0]
for n in range(1, N+1):
    dfs(edges, n, d, f, time)

for n in range(1, N+1):
    print('%d %d %d' % (n, d[n], f[n]))




