H, W = map(int, input().split())

S = [input() for _ in range(H)]
vis = [[-1 for i in range(W)] for j in range(H)]

for v in range(H):
  for h in range(W):
    if v==0:
      if h==0:
        if S[v][h]=="#":
          vis[v][h]=1
        else:
          vis[v][h]=0
      else:
        if S[v][h-1]=="." and S[v][h]=="#":
          vis[v][h] = vis[v][h-1] + 1
        else:
          vis[v][h] = vis[v][h-1]
    else:
      if h==0:
        if S[v-1][h]=="." and S[v][h]=="#":
          vis[v][h] = vis[v-1][h] + 1
        else:
          vis[v][h] = vis[v-1][h]
      else:
        if S[v-1][h]=="." and S[v][h]=="#":
          bufv = vis[v-1][h] + 1
        else:
          bufv = vis[v-1][h]
        if S[v][h-1]=="." and S[v][h]=="#":
          bufh = vis[v][h-1] + 1
        else:
          bufh = vis[v][h-1]
        vis[v][h] = min(bufv, bufh)
    
    #print(vis)
        
print(vis[H-1][W-1])