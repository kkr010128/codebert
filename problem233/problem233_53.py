n=int(input())
a=list(map(int,input().split()))

if n==1:
  print(1)
  
else:
  min1=a[0]
  ans=1
  for x in range(1,n):
    if min1>=a[x]:
      ans+=1
    min1=min(min1,a[x])
    
  print(ans)