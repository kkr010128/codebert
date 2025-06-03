import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = {}
for _ in range(M):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  if a not in edges:
    edges[a] = set()
  if b not in edges:
    edges[b] = set()
  edges[a].add(b)
  edges[b].add(a)

to_check = set(range(N))
max_size = 0
while to_check:
  checked = set()
  s = set()
  s.add(next(iter(to_check)))
  #print(s)
  while s:
    current = s.pop()
    checked.add(current)
    if current in edges:
      for n in edges[current]:
        if n not in checked:
          s.add(n)
  max_size = max(max_size, len(checked))
  #print(checked)
  for c in checked:
    to_check.remove(c)
print(max_size)

