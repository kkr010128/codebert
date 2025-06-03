n=int(input())
s=0
ok=0
for i in range(n):
  lis=input().split()
  if lis[0]==lis[1]:
    s+=1
    if s>=3:
      ok=1
  else:
    s=0
if ok==1:
  print("Yes")
else:
  print("No")