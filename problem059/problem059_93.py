r, c = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(r)]

for i in range(r):
    matrix[i].append(sum(matrix[i]))

matrix.append(list(map(sum, zip(*matrix))))
# matrix.append([sum(i) for i in zip(*matrix)])

for row in matrix:
    print(' '.join(str(e) for e in row))

