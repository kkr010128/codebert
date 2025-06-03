from collections import Counter

input()
a = list(map(int, input().split()))
c = Counter(a)
d = {i: (i * (i - 1)) // 2 for i in set(c.values())}
s = sum(d[i] for i in c.values())
for k in d:
    d[k] = s - d[k] + ((k - 1) * (k - 2) // 2)
d[1] = s
for i in a:
    print(d[c[i]])