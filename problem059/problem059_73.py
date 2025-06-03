def calcTotalOfRowAndCol(matrix, r, c):
    for l in matrix:
        total = 0
        for val in l:
            total += val
        l.append(total)
    matrix.append([])
    for i in range(c + 1):
        total = 0
        j = 0
        while j < r:
            total += matrix[j][i]
            j += 1
        matrix[r].insert(i, total)

    return matrix


if __name__ == '__main__':
    matrix = []
    row, col = [int(x) for x in input().split()]
    i = row
    while i > 0:
        matrix.append([int(y) for y in input().split()])
        i -= 1
    matrix2 = calcTotalOfRowAndCol(matrix, row, col)
    for l in matrix:
        print(' '.join(str(x) for x in l))