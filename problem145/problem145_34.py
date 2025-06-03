from collections import defaultdict
from collections import deque
N, M = map(int, input().split())
edges = defaultdict(list)
ans = [0]*(N+1)
num = 1
q = deque([1])
currentdepth = {1}
nextdepth = set()
for _ in range(M):
  a, b = map(int, input().split())
  edges[a].append(b)
  edges[b].append(a)
while q:
  current = q.popleft()
  for nextver in edges[current]:
    if ans[nextver]==0:
      q.append(nextver)
      ans[nextver] = current
print('Yes')
print(*(ans[2:]),sep='\n')