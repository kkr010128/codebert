n=int(input())
if n%2:
  print(0)
else:
  c=0
  n//=2
  while n:
    n//=5
    c+=n
  print(c)