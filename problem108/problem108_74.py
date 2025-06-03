import sys

n = int(input())

if n % 1000 == 0:
    print(0)
    sys.exit()

while n > 1000:
    n -= 1000

print(1000 - n)