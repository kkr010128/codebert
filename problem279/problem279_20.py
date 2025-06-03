n=int(input())
s=input()

if n%2==1:
  print('No')
  
else:
  t=n//2
  x=s[:t]
  y=s[t:]
  if x==y:
    print('Yes')
  else:
    print('No')