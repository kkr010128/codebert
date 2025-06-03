n = int(input())
p = str(tuple(map(int, input().split())))
q = str(tuple(map(int, input().split())))

import itertools

n_l = [ i+1 for i in range(n) ]
d = {}
for i, v in enumerate(itertools.permutations(n_l)):
    d[str(v)] = i
print(abs(d[p]-d[q]))