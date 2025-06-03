import sys
(a, b, c) = [int(i) for i in sys.stdin.readline().split()]
count = 0
for i in range(a, b + 1):
    if c % i == 0:
        count += 1
print(count)