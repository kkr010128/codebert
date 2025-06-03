import sys

[a, b, c] = [int(x) for x in sys.stdin.readline().split()]
counter = 0
for value in range(a, b + 1):
    if c % value == 0:
        counter += 1

print(counter)