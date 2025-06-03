X,K,D = map(int,input().split())
X = abs(X)

if X >= K*D:
  ans = X - K*D
else:
  k = X // D
  if (K - k) % 2 == 0:
    ans = X - k*D
  else:
    ans = abs(X-(k+1)*D)

print(ans)
