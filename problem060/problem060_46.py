def main():
    N, M, L = map(int, input().split())
    A = tuple(tuple(map(int, input().split())) for _ in range(N))
    B = tuple(tuple(map(int, input().split())) for _ in range(M))

    cell = 0
    row = []
    for n in range(N):
        for l in range(L):
            for m in range(M):
                cell += A[n][m] * B[m][l]
            row.append(cell)
            cell = 0
        print(*row, sep=' ')
        row = []

main()