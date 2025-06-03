X, K, D = list(map(int, input().split()))
X = abs(X)
if(X >= K * D):
  print(X - K * D)
else:
  q = X // D
  r = X % D
  if((K - q) % 2 == 0):
    print(r)
  else:
    print(abs(r - D))
