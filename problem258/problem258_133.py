n=int(input())
if n%2==1:print(0)
else:
  n//=2
  i=5
  s=0
  while i<=n:
    s+=n//i
    i*=5
  print(s)