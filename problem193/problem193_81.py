from collections import deque

H, W, K = map(int, input().split())

mp = [input() for _ in range(H)]

rlt = 1010

h = deque([[1]])

while h:
  t = h.pop()
  if len(t) == H:
    t.append(1)
    tmp = sum(t) - 2
    bs = tmp
    lst = [0]*H
    j = -1
    for i in range(len(t)-1):
      if t[i] == 1:
        j += 1
      lst[i] = j 
    cnt = [0]*(lst[-1]+1)
    for j in range(W):
      tcnt = [0]*(lst[-1]+1)
      f = 0
      for i in range(H):
        tcnt[lst[i]] += int(mp[i][j])
      for k in range(lst[-1]+1):
        if tcnt[k] > K:
          f = 2
          break
        cnt[k] += tcnt[k]
        if cnt[k] > K:
          f = 1
          break
      if f == 2:
        break
      if f == 1:
        tmp += 1
        for k in range(lst[-1]+1):
          cnt[k] = tcnt[k]
    if f < 2:
      rlt = min(rlt, tmp)
    
  else:
    for i in range(2):
      h.append(t+[i])

print(rlt)