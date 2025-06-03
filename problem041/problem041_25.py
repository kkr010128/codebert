W,H,x,y,r = map(int,input().split())
cr = x+r
cl = x-r
ct = y+r
cb = y-r
if ct <= H and cb >= 0 and cl >= 0 and cr <= W:
  print('Yes')
else:
  print('No')