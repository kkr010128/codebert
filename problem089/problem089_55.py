from collections import deque
H, W, M = map(int, input().split())
bomb = []
counth = [0 for k in range(H)]
countw = [0 for k in range(W)]
for k in range(M):
  h, w = map(int, input().split())
  h -= 1
  w -= 1
  bomb.append(h+ w*H)
  counth[h] += 1 
  countw[w] += 1

counth = deque(counth)
countw = deque(countw)

maxh = max(counth)
maxw = max(countw)
index_h = deque([])
index_w = []
for k in range(H):
  h = counth.popleft()
  if h == maxh:
    index_h.append(k)
for k in range(W):
  w = countw.popleft()
  if w == maxw:
    index_w.append(k)

ans = maxh + maxw - 1
lenh = len(index_h)
lenw = len(index_w)

if lenh*lenw > M:
  ans += 1
else:
  bomb.sort()
  bomb = deque(bomb)
  kouho = []
  for i in range(lenh):
    h = index_h.pop()
    for j in range(lenw):
      w = index_w[j]
      kouho.append(h+ H*w)
  kouho.sort()
  kouho = deque(kouho)
  B = bomb.popleft()
  K = kouho.popleft()
  while True:
    if B > K:
      ans += 1
      break
    elif B == K:
      if len(kouho) == 0:
        break
      else:
        K = kouho.popleft()
      if len(bomb) == 0:
        ans += 1
        break
      else:
        B = bomb.popleft()
    else:
      if len(bomb) == 0:
        ans += 1
        break
      else:
        B = bomb.popleft()
print(ans)

