W,H,x,y,r = map(int, input().split())
if(x+r <= W and y+r <= H):
  if(x-r >= 0 and y-r >= 0) :
    print("Yes")
  else :
    print("No")
else :
  print("No")
