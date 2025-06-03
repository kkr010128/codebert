[r,c] = map(int, input().split())
mat = [list(map(int, input().split())) for i in range(r)]
for i in range(r):
    mat[i].append(sum(mat[i]))
r_sum = []
for j in range(c+1):
    r_sum.append(sum([mat[i][j] for i in range(r)]))
for i in range(r):
    print(" ".join(list(map(str, mat[i]))))
print(" ".join(list(map(str, r_sum))))