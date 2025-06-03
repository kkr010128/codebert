a, b, c = (int(i) for i in input().split())
divisor = 0
for i in range(a, b + 1):
  if c % i == 0:
    divisor += 1
print(str(divisor))