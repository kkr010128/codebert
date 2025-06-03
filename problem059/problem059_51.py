table = []
r, c = map(int, input().strip().split())
[table.append(input().strip().split()) for i in range(r)]
table.append([])

for j in range(r + 1):
    for k in range(c + 1):
        if j == r and k != c:
            lastrow = sum(map(int, [table[x][k] for x in range(r)]))
            table[-1].append(lastrow)
        if k == c:
            print(sum(map(int, table[j])))
            break
        print(table[j][k],end=' ')