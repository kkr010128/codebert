#coding: UTF-8
def isPrime(n):
  if n == 1:
    return False
  import math
  m = math.floor(math.sqrt(n))
  for i in range(2,m+1):
    if n % i == 0:
      return False
  return True

n = int(input())
count = 0
for j in range(n):
  m = int(input())
  if isPrime(m):
    count += 1

print(count)
