from collections import deque
n = int(input())
Ps = []
for _ in range(n):
  lis = list(map(int, input().split()))
  if len(lis)>2:
    Ps.append(lis[2:])
  else:
    Ps.append([])
ans = [-1]*n
ans[0] = 0
queue = deque()
checked = deque()
[queue.append([p, 1]) for p in Ps[0]]
checked.append(1)
while queue:
  t, pa = queue.popleft()
  if not t in checked:
    for i in Ps[t-1]:
      queue.append([i, t])
    ans[t-1] = ans[pa-1]+1
    checked.append(t)
for i, a in enumerate(ans):
  print(i+1, a)
