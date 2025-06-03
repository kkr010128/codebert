a,b = map(int,input().split())
k = str(a)
l = str(b)
X = k*b
Y = l*a
if (X < Y):
  print(X)
else:
  print(Y)