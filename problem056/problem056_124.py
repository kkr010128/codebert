N ,M= input().split()
a=[]
N=int(N)
M=int(M)
for i in range(N):
    a.append(list(map(int,input().split())))
b=[int(input()) for i in range(M)]
x=[0 for i in range(N)]
for i in range(N):
    for j in range(M):
        x[i]+=a[i][j]*b[j]
print("\n".join(map(str,x)))