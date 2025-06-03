import math
n = int(input())
a = list(map(int,input().split()))

def generate_D(maxA):
  seq = [i for i in range(maxA+1)]
  p = 2
  while p*p <= maxA:
    if seq[p]==p:
      for q in range(p*2,maxA+1,p):
        if seq[q]==q:
          seq[q] = p
    p += 1
  return seq

cur = a[0]
for v in a[1:]:
  cur = math.gcd(cur,v)
if cur > 1:
  print('not coprime')
else:  
  d = generate_D(max(a))
  primes = set([])
  tf = 1
  for v in a:
    tmp = set([])
    while v > 1:
      tmp.add(d[v])
      v //= d[v]
    for k in tmp:
      if k in primes:
        tf = 0
      else:
        primes.add(k)
  if tf:
    print('pairwise coprime')
  else:
    print('setwise coprime')