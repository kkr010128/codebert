N = int(input())
primes = {}
for num in range(2, int(N**0.5)+1):
  while N%num == 0:
    if num in primes:
      primes[num] += 1
    else:
      primes[num] = 1
    N //= num
ans = 0
for p in primes.values():
  n = 1
  while n*(n+1)//2 <= p:
    n += 1
  ans += n-1
if N > 1:
  ans += 1
print(ans)