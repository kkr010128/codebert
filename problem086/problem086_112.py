N, X, T = list(map(int, input().split(" ")))

result = 0
if N <= X:
  print(T)
elif N % X == 0:
  print((N // X) * T)
else:
  print((N // X) * T + T)