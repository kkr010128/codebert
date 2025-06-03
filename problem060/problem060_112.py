def matprod(A,B):
    C = []
    for i in range(len(A)):
        tmpList = []
        for k in range(len(B[0])):
            tmpVal = 0
            for j in range(len(A[0])):
                tmpVal += A[i][j] * B[j][k]
            tmpList.append(tmpVal)
        C.append(tmpList)
    return C


n,m,l = map(int, input().split())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))

B = []
for i in range(m):
    B.append(list(map(int, input().split())))


for cr in matprod(A,B):
    print(' '.join(map(str, cr)))