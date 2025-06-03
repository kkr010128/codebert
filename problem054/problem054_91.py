from collections import OrderedDict
d = OrderedDict()
d['S'] = set()
d['H'] = set()
d['C'] = set()
d['D'] = set()
a = frozenset(range(1,14))

n = int(input())
for i in range(n):
    s, r = input().split()
    d[s].add(int(r))

for k, v in d.items():
    racks = a.difference(v)
    for rack in racks:
        print(k, rack)