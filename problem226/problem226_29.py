h,n=map(int,input().split())
a=list(map(int,input().split()))

ans=0
if sum(a)>=h:
  print('Yes')
else:
  print('No')