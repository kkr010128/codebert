n,m=map(int,input().split())
a=list(map(int,input().split()))

c=0

for i in a:
  if i>=sum(a)*(1/(4*m)):
    c+=1


if c>=m:
  print('Yes')
else:
  print('No')