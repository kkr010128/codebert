n=int(input())
arr=list(map(int,input().split()))
nxt=1
brk=0
for a in arr:
  if a!=nxt:
    brk+=1
  else:
    nxt+=1
if nxt==1:
  print(-1)
else:
  print(brk)