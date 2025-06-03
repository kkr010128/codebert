import collections

N = int(input())
S = [input() for _ in range(N)]

c = collections.Counter(S)

max_num = max(c.values())

l = []
for item in c.items():
    k = item[0]
    v = item[1]
    if v == max_num:
        l.append(k)

l.sort()

for li in l:
    print(li)
