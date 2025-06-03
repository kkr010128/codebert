n=int(input())
f = False
match=0
for i in range(n):
  a,b=map(int,input().split())
  if a==b:
    match+=1
    f |= (match == 3)
  else:
    match=0
if f:
  print("Yes")
else:
  print("No")