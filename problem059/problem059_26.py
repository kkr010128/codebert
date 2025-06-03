r, c = map(int, input().split())
matrix = []
for _ in range(r):
    L = list(map(int, input().split()))
    matrix.append(L + [sum(L)])
matrix.append([sum(column) for column in zip(*matrix)])
for row in matrix:
    print(' '.join(map(str, row)))