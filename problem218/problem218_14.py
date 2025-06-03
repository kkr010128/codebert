import collections
n=int(input())
s = [(input()) for _ in range(n)]
c = collections.Counter(s)
b = max(c.values())
l = [key for key in c.keys() if c[key] == b]
l.sort()
for i in l:
    print(i)