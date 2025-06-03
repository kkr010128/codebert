def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

n = int(input())
ans = len(make_divisors(n - 1)) - 1
for x in make_divisors(n):
  if x == 1:
    continue
  m = n
  while m % x == 0:
    m //= x
  if m % x == 1:
    ans += 1
print(ans)