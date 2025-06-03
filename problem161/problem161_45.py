a, b, n = map(int, input().split())
if b > n:
  x = n
else:
  x = b - 1
print(int(a * x / b) - a * int(x / b))