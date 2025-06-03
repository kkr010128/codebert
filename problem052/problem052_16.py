import sys

n = int(input())
for i in range(1, n + 1):
  x = i
  if x % 3 == 0:
    sys.stdout.write(" %d" % i)
  else:
    while x > 1:
      if x % 10 == 3:
        sys.stdout.write(" %d" % i)
        break
      x //= 10
print()