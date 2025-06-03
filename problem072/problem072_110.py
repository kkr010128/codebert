n = int(input())
a = 0
b = 0
d1 = 0
d2 = 0
for i in range(n):
  d1,d2 = map(int,input().split())
  if(a==0 and d1 ==d2):
    a+=1
  elif(a==1 and d1 ==d2):
    a+=1
  elif(a==2 and d1 ==d2):
    b +=1
    break
  else:
    a =0
if(b>=1):
  print("Yes")
else:
  print("No")