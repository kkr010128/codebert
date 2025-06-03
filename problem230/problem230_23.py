import sys
readline=sys.stdin.readline

N,D,A=map(int,readline().split())
D*=2 # 爆発の長さ
X=[None]*N
for i in range(N):
  X[i]=list(map(int,readline().split()))

X=sorted(X,key=lambda x:x[0])
# lastX=X[-1][0] # 最後のモンスターの場所
damage=0 # 現在の爆発が与えられるダメージ
from collections import deque
bombs=deque() # 爆弾が切れるタイミング
# [位置、効力]
ans=0
for i in range(len(X)):
  x=X[i][0]
  h=X[i][1] # モンスターの体力
  # 爆発が途切れていないかを確認
  while bombs:
    b=bombs.popleft()
    if b[0]<x:
      damage-=b[1]
    else:
      bombs.appendleft(b)
      break
  h-=damage
  if h>0:
    turn=((h+A-1)//A)
    damage+=turn*A
    ans+=turn
    bombs.append([x+D,turn*A])
print(ans)
