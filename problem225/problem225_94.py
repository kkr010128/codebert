import sys
from itertools import count

H, A = map(int, next(sys.stdin.buffer).split())
for i in count(1):
  H -= A
  if H <= 0:
    break
print(i)