n=int(input())
a=list(map(int,input().split()))

ans=0
ch=1

for x in range(n):
  if a[x]==ch:
    ans+=1
    ch+=1
    
if ans==0:
  print(-1)
else:
  print(n-ans)