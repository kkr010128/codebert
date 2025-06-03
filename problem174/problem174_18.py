from math import gcd
import itertools

k = int(input())

lst = [int(i) for i in range(1, k+1)]
all_array = list(itertools.combinations_with_replacement(lst, 3))
num = 0
for element in all_array:
  a = element[0]
  b = element[1]
  c = element[2]
  d = gcd(gcd(a, b), c)
  if a != b and b != c:
    num += d * 6
  elif a == b and b != c:
    num += d * 3
  elif a != b and b == c:
    num += d * 3
  elif a == b and b == c:
    num += d
print(num)