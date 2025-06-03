n,m,l=map(int,input().split())
matrix_a=[]
matrix_b=[]
matrix_c=[]
for i in range(n):
    matrix_a.append(list(map(int,input().split())))
for i in range(m):
    matrix_b.append(list(map(int,input().split())))
tmp_l=list()
for i in range(n):
    for j in range(l):
        tmp_n=0
        for k in range(m):
            tmp_n+=matrix_a[i][k]*matrix_b[k][j]
        tmp_l.append(tmp_n)
    matrix_c.append(tmp_l.copy())
    tmp_l.clear()
for i in matrix_c:
    tmp=0
    for j in i:
        tmp+=1
        if tmp==l:
            print(j,end="")
        else:
            print(j,"",end="")
    print()