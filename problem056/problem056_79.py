nm = list(map(int, input().split(" ")))
n = nm[0]
m = nm[1]

matrix_A = [list(map(int, input().split(" "))) for i in range(n)]

vector_b = [int(input()) for i in range(m)]

for i in range(n):
    c_i = sum([matrix_A[i][j] * vector_b[j] for j in range(m)])
    print(c_i)