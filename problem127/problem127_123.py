x,y = map(int,input().split())


for i in range(x+1):
  turu = i
  kame = x-i
  if 2 * turu + 4 * kame == y:
    print("Yes")
    break
else :
  print("No")