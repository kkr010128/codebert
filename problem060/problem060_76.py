NML = input().split()
n = int(NML[0])
m = int(NML[1])
l = int(NML[2])

A = []
B = []
for i in range(n):
    A.append([])
    A_r = input().split()
    for j in range(m):
        A[i].append(int(A_r[j]))
for i in range(m):
    B.append([])
    B_r= input().split()
    for j in range(l):
        B[i].append(int(B_r[j]))
for i in range(n):
    for j in range(l):
        out=0
        for k in range(m):
            out +=A[i][k]*B[k][j]
        print(str(out),end="")
        if j != l-1:
            print(" ",end="")
    print("")