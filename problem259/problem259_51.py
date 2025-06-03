import queue

N, U, V = map(int, input().rstrip().split())
U -= 1
V -= 1

v2e = [set() for _ in range(N)]
for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().rstrip().split())
    v2e[a].add(b)
    v2e[b].add(a)
    
q = queue.Queue()
q.put(U)
p = [-1] * N
p[U] = U
while True:
    a = q.get()
    
    if a == V:
        break
    
    for b in v2e[a]:
        if p[b] == -1:
            p[b] = a
            q.put(b)
            
a = V
min_p = []
while True:
    min_p.append(a)
    if a == U:
        break
    a = p[a]

p = [-1] * N
p[min_p[(len(min_p)-1)//2-len(min_p)%2]] = min_p[(len(min_p)-1)//2-len(min_p)%2]
for a in v2e[min_p[(len(min_p)-1)//2-len(min_p)%2]]:
    p[a] = a
p[min_p[-len(min_p)//2+len(min_p)%2]] = min_p[-len(min_p)//2+len(min_p)%2]

q = queue.Queue()
q.put((min_p[-len(min_p)//2+len(min_p)%2], 0))
while q.qsize() > 0:
    a, d = q.get()
    
    for b in v2e[a]:
        if p[b] == -1:
            p[b] = a
            q.put((b, d + 1))
            
print(d + (len(min_p) - 2) // 2 + len(min_p) % 2)