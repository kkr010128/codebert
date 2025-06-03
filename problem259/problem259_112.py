n,u,v = map(int,input().split())

import queue

dist_t = [0] * n
dist_a = [0] * n

elb_t = [0] * n
elb_a = [0] * n

ab = [[] for j in range(n)]

for i in range(n-1):
    a,b = map(int,input().split())
    ab[a-1].append(b-1)
    ab[b-1].append(a-1)

u -= 1
v -= 1

q = queue.Queue()

q.put(u)
elb_t[u] = 1
dist_t[u] = 0

while not q.empty():
    tmp = q.get()
    for i in range(len(ab[tmp])):
        idx = ab[tmp][i]
        if elb_t[idx] != 1:
            if dist_t[idx] != 0:
                dist_t[idx] = min(dist_t[idx], dist_t[tmp] + 1)
            else:
                dist_t[idx] = dist_t[tmp] + 1
            elb_t[idx] = 1
            q.put(idx)

q = queue.Queue()

q.put(v)
elb_a[v] = 1
dist_a[v] = 0

while not q.empty():
    tmp = q.get()
    for i in range(len(ab[tmp])):
        idx = ab[tmp][i]
        if elb_a[idx] != 1:
            dist_a[idx] = dist_a[tmp] + 1
            elb_a[idx] = 1
            q.put(idx)

ans = 0

for i in range(n):
    if dist_a[i] > dist_t[i]:
        ans = max(ans,dist_a[i]-1)

print(ans)