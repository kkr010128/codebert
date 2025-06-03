r,cr,c = map(int,input().split())

matrix_a = [list(map(int,input().split())) for i in range(r)]
matrix_b = [list(map(int,input().split())) for i in range(cr)]
matrix_c = [ [0 for a in range(c)] for b in range(r)]

for j in range(r):
    for k in range(c):
        for l in range(cr):
            matrix_c[j][k] += matrix_a[j][l]*matrix_b[l][k]

for x in matrix_c:
    print(" ".join(list(map(str,x))))