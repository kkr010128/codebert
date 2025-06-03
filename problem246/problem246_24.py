import itertools

n = int(input())
p = map(int, input().split())
q = map(int, input().split())
d = dict()
for i, v in enumerate(itertools.permutations([x for x in range(1, n+1, 1)]), 1):
  d[str(v)] = i

print(abs(d[str(tuple(p))] - d[str(tuple(q))]))
