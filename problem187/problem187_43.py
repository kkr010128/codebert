from collections import deque

n, x, y = map(int, input().split())
a = []

for i in range(1, n + 1):
    if i == 1:
        a.append([2])
    elif i == n:
        a.append([n - 1])
    else:
        a.append([i - 1, i + 1])
a[x - 1].append(y)
a[y - 1].append(x)

d = {}
for i in range(n - 1):
    d[i + 1] = 0

def solve(s):
    queue = deque()
    queue.append(a[s - 1])
    visit = set()
    visit.add(s)
    depth = 0

    while queue:
        depth += 1
        nn = queue.popleft()
        adj = []
        for i in nn:
            if i not in visit:
                d[depth] += 1
                adj = adj + a[i-1]
            visit.add(i)
        if adj != []:
            queue.append(adj)

for i in range(n):
    solve(i + 1)

for i in range(n - 1):
    print(d[i + 1] // 2)
