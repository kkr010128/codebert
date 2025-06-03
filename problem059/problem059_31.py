r, c = map(int, input().split(" "))

table = list()

for i in range(r):

    table.append(list())
    table[i] = list(map(int, input().split(" ")))

    table[i].append(0)
    for j in range(c):
        table[i][c] += table[i][j]

table.append(list())

for i in range(r):
    print(" ".join([str(x) for x in table[i]]))

    for j in range(c + 1):
        if i == 0:
            table[r].append(0)
        table[r][j] += table[i][j]

print(" ".join([str(x) for x in table[r]]))