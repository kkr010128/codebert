# coding: UTF-8
n,m,l = map(int,raw_input().split(" "))
a_matrix = [map(int,raw_input().split()) for i in range(n)]
b_matrix = [map(int,raw_input().split()) for i in range(m)]
tmp3_matrix = []

c_matrix = []
for i in range(n):
    tmp2_matrix = []
    for j in range(l):
        sum = 0
        for k in range(m):
            sum += a_matrix[i][k] * b_matrix[k][j]
        tmp2_matrix.append(sum)
    tmp3_matrix.extend([tmp2_matrix])
c_matrix.extend(tmp3_matrix)
for x in range(n):
    print " ".join(map(str,c_matrix[x]))
