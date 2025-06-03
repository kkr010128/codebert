import collections

N, M = map(int, input().split())

ways = collections.defaultdict(set)
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ways[a].add(b)
    ways[b].add(a)

dist = [-1] * N
q = collections.deque()

dist[0] = True
q.append(0)

while q:
    n = q.popleft()
    for adjacent in ways[n]:
        if dist[adjacent] != -1:
            continue
        dist[adjacent] = dist[n] + 1
        q.append(adjacent)


if -1 in dist:
    print('No')
else:
    print('Yes')
    for n, d in enumerate(dist):
        if n == 0:
            continue
        for adjacent in ways[n]:
            if d - 1 == dist[adjacent]:
                print(adjacent + 1)
                break
