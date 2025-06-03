n, k, d = map(int, input().split())
n = abs(n)
q = n // d
r = n % d
if q >= k:
  print(n - k*d)
else:
  if (k - q) % 2 == 0:
    print(r)
  else:
    print(d - r)