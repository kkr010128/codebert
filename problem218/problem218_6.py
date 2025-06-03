import collections

N = int(input())
L = [input() for i in range(N)]
c = collections.Counter(L)

max_L = max(list(c.values()))

keys = [k for k, v in c.items() if v == max_L]
keys.sort()

for key in keys:
    print(key)
