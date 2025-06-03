n=list(input())
a=0
for i in n:
  a+=int(i)
if a%9==0:
  print('Yes')
else:
  print('No')