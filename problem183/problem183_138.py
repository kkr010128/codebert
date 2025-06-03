import sys
input = sys.stdin.readline
N = int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors
a = make_divisors(N)
b = make_divisors(N - 1)
s = set(a + b)
res = 0
for x in s:
  if x == 1: continue
  t = N + 0
  while t % x == 0: t //= x
  res += (t % x == 1)
print(res)