import math
a,b,c=(int(x) for x in input().split())

x=c-a-b
if x>0:
  if x*x-4*a*b>0:
    print('Yes')
  else:
    print('No')
else:
  print('No')
