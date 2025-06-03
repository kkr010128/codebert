import math
def isprime(x):
  if x == 2:
    return True

  if x < 2 or x % 2 == 0:
    return False

  i = 3
  while i <= math.sqrt(x):
    if x % i == 0:
      return False
    i = i + 2

  return True


count = 0
n = int(input())
for i in range(0, n):
  if isprime(int(input())):
    count += 1

print(count)