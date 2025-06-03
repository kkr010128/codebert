n = int(input())
"""
6:3
3141:13
314159265358:9
"""
#約分
def make_divisors(n):  
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    # divisors.sort()
    return divisors
r = len(make_divisors(n-1)) - 1
w = make_divisors(n)
for wi in w:
  if wi == 1:
    continue
  i = 1
  while n % (wi**i) == 0:
    i += 1
  if (n / (wi**(i-1))) % wi == 1:
    r += 1
print(r)