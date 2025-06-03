n, m, l = [int(x) for x in input().split(" ")]

first = []
second = []

for _ in range(n):
    first.append([int(x) for x in input().split(" ")])

for _ in range(m):
    second.append([int(x) for x in input().split(" ")])

res = []

for i in range(n):
    res.append([])
    for j in range(l):
        a = 0
        for k in range(m):
            a +=(first[i][k] * second[k][j])
        res[i].append(a)

for r in res:
    print(*r)