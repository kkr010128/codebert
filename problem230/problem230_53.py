from collections import deque
n,d,a = map(int,input().split())
c,cc = 0,0
deq = deque()
dl = [tuple(map(int,input().split())) for i in range(n)]
dl.sort()
for i in dl:
  x,h = i
  while deq:
    if deq[0][0] < x-2*d:
      cc -= deq.popleft()[1]
    else:
      break
  h -= a*cc
  if h > 0:
    c += (h-1)//a + 1
    cc += (h-1)//a + 1
    deq.append((x,(h-1)//a + 1))
print(c)