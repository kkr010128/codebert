n=int(input())
cnt=0
ans=0
for i in range(n):
  d1,d2=map(int,input().split())
  if d1==d2:
    cnt=cnt+1
    ans=max(ans,cnt)
  else:
    cnt=0
if ans>=3:
  print("Yes")
else:
  print("No")