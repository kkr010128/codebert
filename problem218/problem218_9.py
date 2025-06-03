N = int(input())

S = [input() for _ in range(N)]

d = {}
for s in S:
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

maxcount = max([d[k] for k in d])
maxlist = list(filter(lambda x: d[x] == maxcount, d))
maxlist = sorted(maxlist)
for m in maxlist:
    print(m)