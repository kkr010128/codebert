def breadth_first_search(G):
  n = len(G)
  d = [-1] * (n + 1)
  d[1] = 0
  queue = [1]

  while len(queue) > 0:
    v = queue.pop(0)
    for c in G[v]:
      if d[c] < 0:
        d[c] = d[v] + 1
        queue.append(c)

  for i in range(1, n + 1):
    print(i, d[i])

G = {}
for i in range(int(input())):
  x = list(map(int, input().split()))
  G[x[0]] = x[2:]

breadth_first_search(G)