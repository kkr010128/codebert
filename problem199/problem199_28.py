s=input()
n=len(s)
if n%2==1:
  print('No')
else:
  fail=0
  for i in range(n):
    if (s[i]!='h' and i%2==0) or (s[i]!='i' and i%2==1):
      fail=1
  if fail==0:
    print('Yes')
  else:
    print('No')