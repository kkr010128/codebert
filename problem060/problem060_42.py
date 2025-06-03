n, m, l = map(int, input().split())

matrix_A = [list(map(int, input().split())) for _ in range(n)]
matrix_B = [list(map(int, input().split())) for _ in range(m)]

matrix_Bt = list(map(list, zip(*matrix_B)))

for a in matrix_A:
    r = []
    for bt in matrix_Bt:
        r.append(sum(x * y for (x, y) in zip(a, bt)))
    print(*r)