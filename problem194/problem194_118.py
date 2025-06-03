H, W = map(int, input().split())

S = [input() for _ in range(H)]
vis = [[-1 for i in range(W)] for j in range(H)]

que = [(0,0)]
itr = 0
color = "."
if S[0][0]=="#":
  itr=1
  color="#"
vis[0][0]=itr
while len(que)>0:
  v, h = que.pop(0)
  itr = vis[v][h]
  if itr%2==0:
    color="."
  else:
    color="#"
  que2 = []
  if v+1 < H:
    if S[v+1][h]==color and vis[v+1][h]==-1:
      vis[v+1][h] = itr
      que2.append((v+1,h))
    elif vis[v+1][h]==-1:
      vis[v+1][h] = itr +1
      que.append((v+1,h))
  if h+1 < W:
    if S[v][h+1]==color and vis[v][h+1]==-1:
      vis[v][h+1] = itr
      que2.append((v,h+1))
    elif vis[v][h+1]==-1:
      vis[v][h+1] = itr+1
      que.append((v, h+1))
  while len(que2)>0:
    v, h = que2.pop(0)
    if v+1 < H:
      if S[v+1][h]==color and vis[v+1][h]==-1:
        vis[v+1][h] = itr
        que2.append((v+1,h))
      elif vis[v+1][h]==-1:
        vis[v+1][h] = itr +1
        que.append((v+1,h))
    if h+1 < W:
      if S[v][h+1]==color and vis[v][h+1]==-1:
        vis[v][h+1] = itr
        que2.append((v,h+1))
      elif vis[v][h+1]==-1:
        vis[v][h+1] = itr+1
        que.append((v, h+1))
    
if vis[H-1][W-1]%2 == 0:
  print(vis[H-1][W-1]//2)
else:
  print((vis[H-1][W-1]+1)//2)