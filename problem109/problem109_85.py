from collections import defaultdict
n = int(input())
d = defaultdict(int)
for i in range(n):
    d[input()] += 1
for v in ['AC', 'WA', 'TLE', 'RE']:
    print(v, 'x', d[v])