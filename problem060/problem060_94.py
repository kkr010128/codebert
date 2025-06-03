n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(m)]

C = []
B_T = list(zip(*B))
for a_row in A:
    C.append([sum(a * b for a, b, in zip(a_row, b_column)) for b_column in B_T])
for row in C:
    print(' '.join(map(str, row)))