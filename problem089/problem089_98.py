H, W, M = map(int, input().split())
h = [0 for _ in range(H+1)]
w = [0 for _ in range(W+1)]
hmax = 0
wmax = 0
Q = []
for _ in range(M):
  a, b = map(int, input().split())
  Q.append((a, b))
  h[a] += 1
  hmax = max(hmax, h[a])
  w[b] += 1
  wmax = max(wmax, w[b])
h_ok = False
w_ok = False
hm = [False for _ in range(H+1)]
wm = [False for _ in range(W+1)]
h_cnt = 0
w_cnt = 0
hw_cnt = 0
for a, b in Q:
  if not hm[a] and h[a] == hmax:
    hm[a] = True
    h_cnt += 1
  if not wm[b] and w[b] == wmax:
    wm[b] = True
    w_cnt += 1
  if h[a] == hmax and w[b] == wmax:
    hw_cnt += 1
if h_cnt*w_cnt - hw_cnt > 0:
  print(hmax+wmax)
else:
  print(hmax+wmax-1)
