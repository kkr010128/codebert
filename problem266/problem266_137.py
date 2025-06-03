X = int(input())

q,mod = divmod(X,100)
if 5*q<mod:
  print(0)
else:
  print(1)