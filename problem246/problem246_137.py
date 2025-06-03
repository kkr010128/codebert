from itertools import permutations
import sys

N = int(sys.stdin.readline().rstrip())
P = [int(x) for x in sys.stdin.readline().rstrip().split()]
Q = [int(x) for x in sys.stdin.readline().rstrip().split()]


def nanba(N, P):
    P = tuple(P)
    for i, p in enumerate(permutations(range(1, N + 1), N)):
        # print(p)
        if P == p:
            return i
    return 0

a = nanba(N, P)
b = nanba(N, Q)

print(abs(a - b))
