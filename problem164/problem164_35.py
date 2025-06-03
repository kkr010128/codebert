a,b,c,d=map(int,input().split())

while True:
  c=c-b
  if c<=0:
  	break
  a=a-d
  if a<=0:
    break
if a>c:
  print('Yes')
else:
  print('No')