from collections import deque

N, D, A = map(int, input().split())
XH = [list(map(int, input().split())) for i in range(N)]

XH.sort(key=lambda x:x[0])

q = deque()

s = 0
ans = 0

for i in range(N):
  x = XH[i][0]
  h = XH[i][1]
  while len(q) > 0:
    elm = q.popleft()
    if x <= elm[0]:
      q.appendleft(elm)
      break
    else:
      s -= elm[1]
  h -= s
  c = max(0, (h + A - 1) // A)
  ans += c
  s += c * A
  q.append((x + 2*D, c*A))
  
print(ans)