a=input().split()
if (a[0]==a[1] and a[1]==a[2] and a[0]==a[2] )or (a[0]!=a[1] and a[1]!=a[2] and a[0]!=a[2]):
  print('No')
else:
  print('Yes')