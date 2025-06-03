nml=input().split()
n,m,l=int(nml[0]),int(nml[1]),int(nml[2])
A_=[input() for i in range(n)]
B_=[input() for i in range(m)]
A,B=[],[]
for i in range(n):
    A_[i]=A_[i].split()
for i in A_:
    A.append(list(map(lambda i:int(i),i)))
for i in range(m):
    B_[i]=B_[i].split()
for i in B_:
    B.append(list(map(lambda i:int(i),i)))
AB=[]
for i in range(n):
    AB.append([])
for i in range(n):
    for j in range(l):
        AB[i].append(0)
for i in range(n):
    for j in range(l):
        for k in range(m):
            AB[i][j]+=(A[i][k]*B[k][j])
for i in AB:
    print(*i)
