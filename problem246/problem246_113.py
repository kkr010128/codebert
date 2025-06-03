from sys import stdin
from itertools import permutations

n = int(stdin.readline().strip())
rank = dict([(val, i) for i, val in enumerate(sorted([int(''.join([str(v) for v in l])) for l in permutations(list(range(1, n+1)), n)])[::-1])])
p_rank = rank[int(''.join(stdin.readline().split()))]
q_rank = rank[int(''.join(stdin.readline().split()))]

print(abs(p_rank - q_rank))