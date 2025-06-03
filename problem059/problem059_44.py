from sys import stdin

r, c = [int(x) for x in stdin.readline().rstrip().split()]
table = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(r)]
for row in range(r):
    table[row] += [sum(table[row])]
    print(*table[row])

col_sum = [sum(x) for x in zip(*table)]
print(*col_sum)
