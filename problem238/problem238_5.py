n, k, s = map(int, input().split())
ans = [s]*k
if s == 10**9:
  ans += [1]*(n-k)
elif s == 1:
  ans += [2]*(n-k)
else:
  ans += [s+1]*(n-k)
print(' '.join(map(str, ans)))