n, m = map(int, input().split())

mat_A = []
vec_b = []

for j in range(n):
    mat_A.append(list(map(int, input().split())))
for i in range(m):
    vec_b.append(int(input()))

for j in range(n):
    tmp = 0
    for i in range(m):
        tmp += mat_A[j][i] * vec_b[i]
    print(tmp)