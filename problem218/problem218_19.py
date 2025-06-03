N = int(input())
S = [input() for i in range(N)]
d = {}
m = 0
for i in S:
    if i in d:
        d[i] += 1
        if d[i] > m:
            m = d[i]
    else:
        d[i] = 1
        
d = dict(sorted(d.items(), reverse=True))
a = {}
for i in d.keys():
    if m <= d[i]:
        a[i] = 0
a = sorted(a)
for i in a:
    print(i)