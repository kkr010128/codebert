N=int(input())
cnt=0
ans="No"
for i in range(N):
  x,y=input().split()
  if x==y:
    cnt=cnt+1
  else:
    cnt=0
  if cnt>=3:
    ans="Yes"
print(ans)