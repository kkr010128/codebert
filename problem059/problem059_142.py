(r, c) = [int(i) for i in input().split()]

table = [[0 for j in range(c + 1)]for i in range(r + 1)]

for i in range(r):
    tmp = [int(x) for x in input().split()]
    for j in range(c + 1):
        if not j == c:
            table[i][j] = tmp[j]
            table[i][c] += table[i][j]
        table[r][j] += table[i][j]

for i in range(r + 1):
    for j in range(c + 1):
        if j == c:
            print(table[i][j], end='')
        else:
            print(table[i][j], '', end='')
    print()