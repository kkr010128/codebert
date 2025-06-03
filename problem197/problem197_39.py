a,b,c=map(int,input().split())
s=(c-a-b)*(c-a-b)-4*a*b
if s>0 and c-a-b>0:
  print('Yes')
else:
  print('No')