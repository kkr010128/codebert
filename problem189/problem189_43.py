import math
n, m = map(int, input().split())

if n >= 2:
  a = math.factorial(n)/(math.factorial(2)*math.factorial(n-2))
else:
  a = 0

if m >= 2:
  b = math.factorial(m)/(math.factorial(2)*math.factorial(m-2))
else:
  b = 0

print(int(a + b))