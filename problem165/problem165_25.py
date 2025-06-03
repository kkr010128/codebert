import collections

n = int(input())
s = [input() for i in range(n)]
t = collections.Counter(s)

print(len(t))