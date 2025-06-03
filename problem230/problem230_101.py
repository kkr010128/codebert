from collections import deque
N, D, A = map(int, input().split())
ls = []
for i in range(N):
  x,h = map(int, input().split())
  h = h//A if h%A==0 else h//A+1
  ls += [(x,h)]
ls.sort(key=lambda x:x[0])
deq = deque([])
ans = 0
acc = 0
for i in range(N):
  x, h = ls[i]
  while deq and deq[0][0]<x:
    y, d = deq.popleft()
    acc -= d
  n = max(0,h-acc)
  ans += n
  acc += n
  if n:
    deq += [(x+2*D,n)]
print(ans)