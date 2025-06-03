X,Y=list(map(int,input().split()))
judge=False
for i in range(0,X+1):
  if i*2+(X-i)*4==Y:
    judge=True
if judge:
  print("Yes")
else:
  print("No")