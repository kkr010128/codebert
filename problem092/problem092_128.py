x,k,d=map(int,input().split())
if abs(x) >=k*d:
  print(abs(x)-k*d)
else:
  c = x//d
  k -= c
  x %= d
  if k % 2:print(d-x)
  else:print(x)