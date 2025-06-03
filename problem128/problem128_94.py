X,N = map(int, input().split())
P = list(map(int, input().split()))

if len(P) == 0:
  print(X)
else:
  for i in range(0,10000):
    if P.count(X-i) == 0:
      print(X-i)
      break
    elif P.count(X+i) == 0:
      print(X+i)
      break
    else:
      continue