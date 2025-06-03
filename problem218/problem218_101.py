import collections

n = int(input())
words = []
for i in range(n):
    words.append(input())

c = collections.Counter(words)

values, counts = zip(*c.most_common())

nums = counts.count(max(counts))
xs = (list(values))[:nums]
xs.sort()

for x in xs:
    print(x)