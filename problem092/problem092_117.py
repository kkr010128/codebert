X, K, D = map(int, input().split())

X = abs(X)
if X >= K * D:
  ans = X - K * D

else:
  n, d = divmod(X, D)
  ans = d
  if (K - n) % 2:
    ans = D - d


print(ans)