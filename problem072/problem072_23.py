n=int(input())
flag=0
for i in range(n):
  a=list(map(int,input().split()))
  if a[0]==a[1]:
    flag+=1
  else:
    flag=0
  if flag==3:
    break
if flag==3:
  print("Yes")
else:
  print("No")