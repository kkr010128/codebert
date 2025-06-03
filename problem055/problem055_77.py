from collections import OrderedDict
from itertools import cycle, islice
 
d = OrderedDict(("{} {} {}".format(b, f, r), 0) for b in range(1, 5)
                                                for f in range(1, 4)
                                                for r in range(1, 11))
 
n = int(input())
for _ in range(n):
    s = input()
    idx = s.rfind(" ")
    d[s[:idx]] += int(s[idx+1:])

data = d.values()
delim = "#" * 20
for i in range(0, 120, 10):
    print(" " + " ".join(map(str, islice(cycle(data), i, i+10))))
    if i in (20, 50, 80):
        print(delim)