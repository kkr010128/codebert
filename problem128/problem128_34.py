X, N = map(int, input().split())
 
ans = 0
if N > 0:
  p = list(map(int, input().split()))
  r = [i for i in range(102) if i not in p]
  d = [abs(X-i) for i in r]
  ans = r[d.index(min(d))]
else:
  ans = X

print(ans)