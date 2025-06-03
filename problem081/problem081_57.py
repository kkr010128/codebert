D,T,S=map(int,input().split())
if 1<=D<=10000 and 1<=T<=10000 and 1<=S<=10000:
  if (D/S)>T:
    print("No")
  else:
    print("Yes")