import math

N = int(input())

def enumerate_divisors(N):
  all_divisors = set()
  for divisor in range(1, int(math.sqrt(N)) + 1):
    if N%divisor == 0:
      if divisor == 1:
        all_divisors.add(N/divisor)
      else:
        all_divisors = all_divisors | {divisor, N/divisor}

  all_divisors = list(all_divisors)
  return all_divisors

def calculate_reminder(N, d):
  while True:
    reminder = N%d
    if reminder == 0:
      N /= d
    else:
      return reminder

if N == 2:
  counter = 1
else:
  counter = len(enumerate_divisors(N-1))
  for div in enumerate_divisors(N):
    if calculate_reminder(N, div) == 1:
      counter += 1

print(counter)