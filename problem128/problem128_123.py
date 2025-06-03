X,N = map(int,input().split())
p = list(map(int, input().split()))

i = 0

if X not in p:
  print(X)

else:
  while True:
    i += 1
    if X - i not in p:
      print(X-i)
      break
    if X+i not in p:
      print(X+i)
      break
