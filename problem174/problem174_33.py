def gcd(x, y):
  if y==0: return x
  return gcd(y, x%y)
K = int(input())
res = 0
for a in range(1, K+1):
  for b in range(a, K+1):
    for c in range(b, K+1):
      if len(set([a, b, c]))==3: res += gcd(gcd(a, b), c) * 6
      elif len(set([a, b, c]))==2: res += gcd(gcd(a, b), c) * 3
      else: res += gcd(gcd(a, b), c)
print(res)