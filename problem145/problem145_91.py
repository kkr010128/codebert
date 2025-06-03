from collections import deque
import sys
N, M = list(map(int, input().split()))
ans = [-1] * N
visited = [False] * N
dq = deque([0])
path = [[] for _ in range(N)]
for s in sys.stdin.readlines():
    a, b = list(map(lambda x: int(x)-1, s.split()))
    path[a].append(b)
    path[b].append(a)
while dq:
   i = dq.popleft()
   if visited[i]:
      continue
   visited[i] = True
   next_rs = path[i]
   for j in range(len(next_rs)):
      if not visited[next_rs[j]]:
         dq.append(next_rs[j])
         if ans[next_rs[j]] == -1:
            ans[next_rs[j]] = i
if sum(visited) == N:
   print('Yes')
   for i in range(N):
      if i == 0:
         continue
      else:
         print(ans[i]+1)
else:
   print(-1)