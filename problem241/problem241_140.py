H, W = map(int, input().split())
#外壁として障害物置く
H += 2
W += 2
P = [[] for _ in range(H*W)]

move = [(0, 1), (1, 0), (-1, 0), (0, -1)]

for y in range(1, H-1):
  for x in range(1, W-1):
    for z in move:
      P[x+W*y].append(x+z[0]+W*(y+z[1]))

for y in range(H-2):
  L = input()
  for x, s in enumerate(L):
    if s == "#":
      P[x+1 + W*(y+1)] = []

def bfs(x, y):
    s = x + W*y
    d = [-1] * (H*W)
    d[s] = 0
    p_old = [s]
    cnt = 1
    m_cnt = 0
    last = 1
    #print(d, p_old)
    while p_old:
      p_new = []
      for i in p_old:
        for j in P[i]:
          if d[j] == -1 and P[j] != []:
            d[j] = cnt
            m_cnt = max(m_cnt, cnt)
            p_new.append(j)
      p_old = p_new
      cnt += 1
      #print(d, p_old)
    return m_cnt

ans = 0

for y in range(1, H-1):
  for x in range(1, W-1):
    ans = max(ans, bfs(x, y))

print(ans)