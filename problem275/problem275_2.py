x,y = map(int,input().split())
if(x+y==2):
  print(1000000)
else:
  answer = 0
  if(x==2):
    answer+=200000
  elif(x==3):
    answer+=100000
  elif(x==1):
    answer+=300000
  if(y==2):
    answer+=200000
  elif(y==3):
    answer+=100000
  elif(y==1):
    answer+=300000
  print(answer)
