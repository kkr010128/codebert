r, c = map(int, input().split())
table = []
for i in range(r):
    table.append(list(map(int, input().split())))
for i in table:
    i.append(sum(i))
b = []
for i in range(c):
    x = 0
    for k in range(r):
        x += table[k][i]
    b.append(x)
b.append(sum(b))
for i in table:
    print(" ".join(map(str, i)))
print(" ".join(map(str, b)))
