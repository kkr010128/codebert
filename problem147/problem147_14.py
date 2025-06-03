s=input()
t=input()
n=len(s)
if s==t[:n] and len(t)==n+1:
  print('Yes')
else:
  print('No')