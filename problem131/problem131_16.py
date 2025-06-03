A,V = map(int,input().split(" "))
B,W = map(int,input().split(" "))
T, = map(int,input().split(" "))
kyori = abs(A-B)
dif = V-W
if dif>0:
  if kyori/dif<=T:
    print("YES")
  else:
    print("NO")
else:
  print("NO")