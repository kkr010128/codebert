X, K, D = map(int, input().split())
absX = abs(X)
step = min(K, (absX // D))

if K > step:
  extra = - D * ((K - step) % 2)
else:
  extra = 0

print(abs(absX - step * D + extra))