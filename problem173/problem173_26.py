import sys
n = int(sys.stdin.read())
print(sum(i for i in range(1, n + 1) if i % 3 and i % 5))