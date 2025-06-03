from math import sqrt

a, b, c = map(int, input().split())

d = c - a - b

print('Yes' if d > 0 and d ** 2 > 4 * a * b  else 'No')


