X,N = map(int,input().split())
P = list(map(int,input().split()))

if N == 0:
  print(X)
else:
  for i in range(X,-2,-1):
    if i not in P:
      a = abs(X - i)
      break
  for j in range(X+1,102):
    if j not in P:
      b = abs(j - X)
      break
  if a <= b:
    print(i)
  else:
    print(j)