import sys
import collections

S = int(next(sys.stdin))
_A = (s.strip() for s in sys.stdin)
A = collections.Counter(_A)

# print(A)
# print(max(A.values()))

m = max(A.values())
keys = [k for k, v in A.items() if v == m]
keys.sort()
for s in keys:
  print(s)