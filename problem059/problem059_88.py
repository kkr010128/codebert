r, c = [int (x) for x in input().split(' ')]
a = [[0 for i in range(c)] for j in range(r)]
for s in range(0,r):
    a[s] = [int (x) for x in input().split(' ')]

for tr in range(0,r):
    total = 0
    for v in a[tr]:
        total += v
    a[tr].append(total)

total = [0 for i in range(c+1)]
for tr in range(0,r):
    for tc in range(0,c+1):
        total[tc] += a[tr][tc]
a.append(total)

for i in range(r+1):
    a[i] = [str(a[i][j]) for j in range(c+1)]
    print(' '.join(a[i]))