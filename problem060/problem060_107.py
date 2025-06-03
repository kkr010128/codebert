n,m,l=map(int,input().split())
a = [[0 for i in range(m)] for j in range(n)]
#print(a)
b = [[0 for i in range(1)] for j in range(m)]
#print(b)
A=[]
B=[]
for j in range (n):
    a = [int(x) for x in input().split()]
    A.append(a)
#print(A)
for i in range(m):
    b = [int(y) for y in input().split()]
    B.append(b)
#print(B)
#print(A[1][1])
for j in range (0,n):
        F=[]
        #print(j)
        for k in range (0,l):
            S=0
            for i in range (0,m):
                B1=B[i][k]
                A1=A[j][i]
        #print(A1)
                #print(A1,B1,sep=" ")
                S=S+int(A1)*int(B1)
            F.append(S)
            #print(S,end='')
            #rint('@',end='')
        print(*F)
