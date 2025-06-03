N, X, T = map(int, input().split())

t = N % X
s = N // X

if t != 0:
  print(T * (s + 1))
  
else:
  print(T * s)