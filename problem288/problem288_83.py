n = int(input())
root = int(n**0.5)
a = 0

for i in range(root, 0, -1):
  if n % i == 0:
    a = i
    break

b = n // a
print(a+b - 2)
