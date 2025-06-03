n=int(input())
xy=[[] for i in range(n)]
for i in range(n):
  a=int(input())
  for j in range(a):
    x,y=map(int,input().split())
    x-=1
    xy[i].append((x,y))
ans=0
for i in range(1<<n):
  cnt=bin(i).count("1")
  if cnt<=ans:continue
  for j in range(n):
    if i&(1<<j):
      for x,y in xy[j]:
        if y==1 and i&(1<<x):continue
        if y==0 and i&(1<<x)==0:continue
        break
      else:
        continue
      break
  else:
    ans=cnt
print(ans)




