X, K, D = map(int, input().split())

value = abs(X)

if (value / D) >= K:
  print(value - D * K)
else:
  min_count = value // D
  mod_value = K - min_count
  if mod_value % 2 == 0:
    print(value % D)
  else:
    print(abs(value % D - D))