n, a, b = map(int, input().split())
d = n // (a + b)
q = n % (a + b)
if q <= a:
  count = d * a + q
else:
  count = d * a + a
print(count)