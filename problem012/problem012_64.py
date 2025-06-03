import sys
import math


prime_numbers = [2, 3, 5, 7]

def prime_numbers_under(num):
  global prime_numbers

  prime_number_max = max(prime_numbers)
  if prime_number_max > num:
    return prime_numbers

  for i in range(prime_number_max + 1, num + 1):
    check_max = math.floor(math.sqrt(i))
    for j in prime_numbers:
      if j <= check_max:
        if i % j == 0:
          break
    else:
      prime_numbers.append(i)

  return prime_numbers

def main():
  amount = 0

  length = int(input())
  for _ in range(0, length):
    i = int(input())
    check_max = math.floor(math.sqrt(i))
    for j in prime_numbers_under(check_max):
      if j <= check_max:
        if i % j == 0:
          break
    else:
      amount += 1

  print(amount)
  return 0


if __name__ == '__main__':
  main()