r, c = map(int, input().split())
table = []
for _ in range(r):
    table.append(list(map(int, input().split())))
for row in range(r):
    print(' '.join(map(str, table[row])), sum(table[row]), sep=' ')
# print(' '.join(map(str, [sum(table[:][col]) for col in range(c)])), sum(table), sep=' ')
col_sum = [sum([table[row][col] for row in range(r)]) for col in range(c)]
print(' '.join(map(str, col_sum)), sum(col_sum), sep=' ')

