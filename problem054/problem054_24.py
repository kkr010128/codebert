n=input()
s=[[1 for i in range(13)] for j in range(4)]
for i in range(n):
  a,b=map(str,raw_input().split())
  b=int(b)
  if a=='S':s[0][b-1]=0
  elif a=='H':s[1][b-1]=0
  elif a=='C':s[2][b-1]=0
  else:s[3][b-1]=0
for i in range(4):
  for j in range(13):
    if s[i][j]:
      if i==0:print'S',j+1
      if i==1:print'H',j+1
      if i==2:print'C',j+1
      if i==3:print'D',j+1