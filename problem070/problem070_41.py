import queue
n, m = map(int, input().split())
a = [[] for _ in range(n)]
ans = 0
 
for _ in range(m):
    x, y = map(int, input().split())
    a[x-1].append(y-1)
    a[y-1].append(x-1)
 
route = set()
route.add(0)
q = queue.Queue()
q.put(0)
 
for i in range(n):
    if not i in route:
        route.add(i)
        q.put(i)
        ans += 1
    while not q.empty():
        c = q.get()
        for k in a[c]:
            if not k in route:
                q.put(k)
                route.add(k)
    if len(route) == n:
        print(ans)
        break