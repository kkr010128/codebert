X,Y=list(map(int, input().split()))
b=(Y-2*X)/2
a=X-b
if int(a)==a and int(b)==b and a>=0 and b>=0:
  print('Yes')
else:
  print('No')