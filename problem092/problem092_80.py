X,K,D = map(int,input().split())
X = abs(X)
ans = 0

if X>=D and D*K<=X:
  ans = X - D*K
if X>=D and D*K>X:
  K=K-int(X/D)
  X=X%D
  if K%2==0:
    ans=X
  else:
    ans = abs(X-D)
if X<D:
  if K%2==0:
    ans = X
  else:
    ans = abs(X-D)

print(ans)  