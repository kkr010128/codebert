import sys
input = sys.stdin.readline

n, res = int(input()), 0
for i in range(1, n + 1): res += 0 if i % 3 == 0 or i % 5 == 0 else i
print(res)