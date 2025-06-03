from math import factorial
a = 0
b = 0
n, m = map(int,input().split())
if 1 < n:
  a = factorial(n) / factorial(2) / factorial(n - 2)
if 1 < m:
  b = factorial(m) / factorial(2) / factorial(m - 2)
print(int(a+b))