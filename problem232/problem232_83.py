a, b = map(int, input().split())
alpha = str(b)
beta = str(a)
if a >= b:
  for k in range(a - 1):
    alpha = alpha + str(b)
  print(int(alpha))
else:
  for k in range(b - 1):
    beta = beta + str(a)
  print(beta)