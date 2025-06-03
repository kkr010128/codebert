cin = open(0).read().strip().split('\n')
n = int(cin[0])
v = [list(map(lambda x: int(x)-1, a.split(' ')[2:])) for a in cin[1:]]

import queue
q = queue.Queue()
q.put(0)

dist = [-1]*n
dist[0] = 0
seen = [False]*n
while not q.empty():
    num = q.get()
    seen[num] = True
    for a in v[num]:
        if dist[a] != -1: continue
        dist[a] = dist[num] + 1
        q.put(a)

for idx, num in enumerate(dist):
    print(idx+1, num)
