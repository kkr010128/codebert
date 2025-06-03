n, m, l = map(int, input().split())
mat_a = []
mat_b = []

for i in range(n):
    mat_a.append(list(map(int, input().split())))
    
for j in range(m):
    mat_b.append(list(map(int, input().split())))
    
for p in range(n):
    mat_c = []
    for q in range(l):
        sum = 0
        for r in range(m):
            sum += mat_a[p][r] * mat_b[r][q]
        mat_c.append(sum)
    print(' '.join(map(str, mat_c)))



