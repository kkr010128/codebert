from collections import Counter

a = map(int, input().split())
c = Counter(a)
d = {1: 300000, 2: 200000, 3: 100000}

ret = sum(c[rank] * d[rank] for rank in range(1, 3 + 1))
if c[1] == 2:
    ret += 400000
print(ret)
