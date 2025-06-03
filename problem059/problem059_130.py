r, c = [int(_) for _ in input().split()]
sum_row = [0 for _ in range(c + 1)]
for i in range(r):
    row = [int(_) for _ in input().split()]
    row.append(sum(row))
    print(*row)
    for j in range(c + 1):
        sum_row[j] += row[j]
print(*sum_row)
