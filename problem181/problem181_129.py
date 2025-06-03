import sys
readline = sys.stdin.readline

K = int(readline())

from collections import deque
q = deque([i for i in range(1,10)])

cnt = 0
while q:
  n = q.popleft()
  cnt += 1
  if cnt == K:
    print(n)
    break
  right = n % 10
  for c in range(max(right - 1, 0),min(right + 2,10)):
    q.append(n * 10 + c)
    
