from math import sqrt, ceil
n = int(input())
def ans(n):
  if n == 2:
    return 1
  # divisors of n-1
  count = sum(2*int((n-1)%i==0) for i in range(2, ceil(sqrt(n-1))))
  # check the square root of n-1
  if ceil(sqrt(n-1)) == int(sqrt(n-1)):
    count += 1
  # n-1 is always a divisor of n-1
  count += 1
  # divisors of n
  for i in range(2, ceil(sqrt(n))):
    if n%i==0:
      x = n
      while x%i == 0:
        x = x//i
      count += int((x-1)%i==0)
      other_divisor = n//i
      x = n
      while x%other_divisor == 0:
        x = x//other_divisor
      count += int((x-1)%other_divisor==0)
  # check the square root of n
  if ceil(sqrt(n)) == int(sqrt(n)):
    i = int(sqrt(n))
    x = n
    while x%i == 0:
      x = x//i
    count += int((x-1)%i==0)
  # n is always a divisor of n that reduces to 1 by division once
  count += 1
  return(count)
print(ans(n))