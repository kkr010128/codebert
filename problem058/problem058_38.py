import itertools
a = []
while True:
    n = map(int, raw_input().split())
    if n == [0, 0]:
        break
    a.append(n)

for n in range(len(a)):
    x = 0
    b = []
    for m in range(a[n][0]):
        if m == range(a[n][0]): break
        b.append(m+1)

    c = list(itertools.combinations(b, 3))
    for l in range(len(c)):
        sum = c[l][0] + c[l][1] + c[l][2]
        if sum == a[n][1]: x += 1
    print x