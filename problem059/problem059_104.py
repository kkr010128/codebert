r, c = map(int, input().split())
a = [list(map(int, input().split())) for i in range(r)]
newr = []

for i in range(r):
    a[i].append(sum(a[i]))

for j in range(c + 1):
    sumc = 0
    for i in range(r):
        sumc += a[i][j]
    newr.append(sumc)
a.append(newr)

for i in range(r+1):
    print(" ".join(str(t) for t in a[i]))