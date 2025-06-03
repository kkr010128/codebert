import collections
N = int(input())
S = []
for i in range(N):
    s = input()
    S.append(s)
c = collections.Counter(S)
values, counts = zip(*c.most_common())
print(len(values))