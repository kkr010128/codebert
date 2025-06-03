a,b,c=map(int,input().split())
k=int(input())
i=0
while True:
  if a<b:
    break
  b*=2
  i+=1
while True:
  if b<c:
    break
  c*=2
  i+=1
if i<=k:
  print("Yes")
elif i>k:
  print("No")