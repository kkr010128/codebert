from collections import defaultdict
N = int(input())
d = defaultdict(int)
for i in range(1, N+1):
    s = str(i)
    top = int(s[0])
    end = int(s[-1])
    d[(top, end)] += 1
counter = 0
for i in range(1, N+1):
    s = str(i)
    top = int(s[0])
    end = int(s[-1])
    if (end, top) in d:
        counter += d[(end, top)]
print(counter)