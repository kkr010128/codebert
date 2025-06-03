from collections import defaultdict
import sys
N = int(input())

A = list(map(int, input().split()))

C = defaultdict(int)

for a in A:
  C[a] += 1
  if C[a] >= 2:
    print('NO')
    sys.exit()

print('YES')