import sys
readline = sys.stdin.buffer.readline

N = int(readline())
P = list(map(int, readline().split()))
Q = list(map(int, readline().split()))

from itertools import permutations

p = list(permutations(range(1, N+1)))

# print(p)

a = p.index(tuple(P))
b = p.index(tuple(Q))

print(abs(a-b))
