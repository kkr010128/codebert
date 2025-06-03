import math

n, m = map(int, input().split())
r = 2

if (n > 1):
  cn = math.factorial(n) / (2 * math.factorial(n - r))
else:
  cn = 0
  
if (m > 1):
  cm = math.factorial(m)  / (2 * math.factorial(m - r))
else :
  cm = 0
  
print(int(cn+cm))