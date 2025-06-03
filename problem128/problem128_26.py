X,N=map(int,input().split())
if N>0:
  P=list(map(int,input().split()))
  for i in range(N+1):
    if X-i not in P:
      print(X-i)
      break
    elif X+i not in P:
      print(X+i)
      break
else:
  print(X)