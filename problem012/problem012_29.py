def getprimes(n):
  primes = []
  for i in xrange(2, n+1):
    isprime = True
    for j in xrange(len(primes)):
      if i % primes[j] == 0:
        isprime = False
        break
    if isprime:
      primes.append(i)
  return primes

n = int(raw_input())
primes = getprimes(10000)
count = 0
for _ in xrange(n):
  x = int(raw_input())
  isprime = True
  for i in xrange(len(primes)):
    if primes[i] >= x:
      break
    if x % primes[i] == 0:
      isprime = False
      break
  if isprime:
    count += 1
print count