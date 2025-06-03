import sys
n = int(sys.stdin.readline().rstrip("\n"))
if n % 2 == 0:
    print(n // 2)
else:
    print(n // 2 + 1)