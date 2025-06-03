X, K, D = map(int,  input().split())
X = abs(X)
if K%2 == 1:
  K -= 1
  X -= D
  
K_ = K // 2

min_Y = X - K_ * (2 * D)

if min_Y > 0:
  print(min_Y)
else:
  min_Y_p = X % (2 * D)
  min_Y_m = 2 * D - X % (2 * D)
  print(min(min_Y_p, min_Y_m ))