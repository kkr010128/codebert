import math
a, b, n = list(map(int, input().split()))
output = 0
if n < b:
  output = math.floor(a * n / b)
else:
  output = math.floor(a * (b-1) / b)
print(output)