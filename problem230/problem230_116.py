from collections import deque
n, d, a = map(int, input().split())
XH = [list(map(int, input().split())) for _ in range(n)]
XH.sort()
# X:座標、 C:倒すための必要爆発回数
XC = [[x, (h - 1) // a + 1] for x, h in XH]
      
q = deque([])
accum_dmg = 0
ans = 0

for x, c in XC:
  # q[-][0]は爆発が届く右端の座標
  # 爆発が届いていない地点に来たら累積ダメージを減らす
  while q and x > q[0][0]:
    _, dmg = q.popleft()
    accum_dmg -= dmg
    
  cnt = max(0, c - accum_dmg)
  ans += cnt
  accum_dmg += cnt
  
  if cnt:
    q.append([x + 2 * d, cnt])
print(ans)