n,M = list(map(int,input().split()))

m = [[] for _ in range(n)]
dp = [0]*n
from collections import deque
que = deque()
for _ in range(M):
  a,b = map(int,input().split())
  a -= 1
  b -= 1
  m[a].append(b)
  m[b].append(a)
  if a == 0:
    que.append(b)
    dp[b] = 1
  if b == 0:
    que.append(a)
    dp[a] = 1

while que:
  c = que.popleft()
  for i in m[c]:
    if dp[i] == 0 :
      dp[i] = c+1
      que.append(i)

#[exit(print('No')) for i in range(1,n)  if dp[i] == 0]

print('Yes')
[print(dp[i]) for i in range(1,n)]
