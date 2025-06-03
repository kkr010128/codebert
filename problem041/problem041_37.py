W,H,x,y,r = map(int,input().split())

if (r <= y and y <= H-r) :
  if (r <= x and x <= W-r ):
    print('Yes')
  else :
    print('No')
else :
  print('No')
