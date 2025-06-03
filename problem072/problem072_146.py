n=int(input())
f=False
c=0
for i in range(n):
  a,b=map(int,input().split())
  if a==b:
    c+=1
    if c==3:
      f=True
      break
  else:
    c=0
if f:
  print("Yes")
else:
  print("No")