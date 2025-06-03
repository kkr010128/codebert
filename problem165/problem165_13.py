import collections
N = int(input())
ls = []
for i in range(N):
    ls.append(input())
counter = collections.Counter(ls)
print(len(counter.keys()))