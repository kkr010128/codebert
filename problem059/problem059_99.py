n,m = map(int,(input().split()))
a = []
s = []
for i in range(m):
    s.append(0)

for i in range(n):
    k = [int(i) for i in input().split()]
    k.append(sum(k))
    a.append(k)
    for j in range(m):
        s[j] += k[j]

s.append(sum(s))
a.append(s)

for j in a:
    print(' '.join(map(str, j)))