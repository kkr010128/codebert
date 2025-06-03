H,A=map(int,input().split())
if H%A>0:
  print((H//A)+1)
elif H%A==0:
  print(H//A)