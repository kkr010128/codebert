import math


def is_prime(n):
  if n in [2, 3, 5, 7]:
    return True
  elif 0 in [n%2, n%3, n%5, n%7]:
    return False
  else:
    check_max = math.ceil(math.sqrt(n))
    for i in range(2, check_max + 1):
      if n % i == 0:
        return False
    else:
      return True

def main():
  primes = set([])
  length = int(input())
  for _ in range(0, length):
    n = int(input())
    if is_prime(n):
      primes.add(n)

  print(len(primes))
  return 0


if __name__ == '__main__':
  main()