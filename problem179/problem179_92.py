n,m=map(int,input().split())
a=list(map(int,input().split()))
s = sum(a)
ans =0
for i in a:
  if i>=s/4/m:
    ans+=1

if ans>=m:
  print('Yes')
else:
  print('No')
