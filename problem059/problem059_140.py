import sys
from operator import add
(r, c) = [int(i) for i in sys.stdin.readline().split()]
s = [0] * (c + 1)
for i in range(r):
    l = [int(i) for i in sys.stdin.readline().split()]
    l.append(sum(l))
    print(" ".join([str(i) for i in l]))
    s = map(add, s, l)

print(" ".join([str(i) for i in s]))