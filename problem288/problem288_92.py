import math
N = int(input())

def mass_search(x):
  divisor = 0
  limit = math.floor(math.sqrt(x))
  for i in range(1,limit+1):
    if N % i == 0:
      divisor = max(divisor, i)
  x = divisor
  y = N//divisor
  return x+y-2

print(mass_search(N))