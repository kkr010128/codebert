import math
from itertools import permutations

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

ls = permutations(range(1, N+1), N)

Ns = []

for l in ls:
    s = ''.join([str(n) for n in l])
    Ns.append(int(s))

p = ''.join(map(str, P))
q = ''.join(map(str, Q))

a = Ns.index(int(p)) + 1
b = Ns.index(int(q)) + 1

print(abs(a-b))

