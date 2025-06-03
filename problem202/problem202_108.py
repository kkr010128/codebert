N,A,B = map(int, input().split())
X = N//(A+B)
Y = N%(A+B)
if Y < A:
  print(A*X+Y)
else:
  print(A*(X+1))