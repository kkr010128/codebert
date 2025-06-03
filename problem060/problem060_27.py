def main():

    n, m, l = map(int, input().split())
    matrix_a = [list(map(int, input().split())) for i in range(n)]
    matrix_b = [list(map(int, input().split())) for j in range(m)]
    matrix_c = [[0 for i in range(l)] for j in range(n)]
    for i in range(n):
        for j in range(l):
            matrix_c[i][j] = sum(matrix_a[i][k] * matrix_b[k][j] for k in range(m))

    for row in matrix_c:
        print(' '.join(map(str, row)))

main()