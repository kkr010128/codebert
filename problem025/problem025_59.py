import itertools
n=int(input())
A=[0 for i in range(n)]
A=input().split()
for i in range(n):
    A[i]=int(A[i])
q=int(input())
B=[0 for i in range(q)]
B=input().split()
C=[]
for i in range(q):
    B[i]=int(B[i])
l=[0,1]
p=[]
k=0
D=[]
for v in itertools.product(l,repeat=n):
    sum=0
    for i in range(n):
        if v[i]==1:
            sum=sum+A[i]
    D.append(sum)
    k+=1
for i in range(q):
    if B[i] in D:
        C.append("yes")
    else:
        C.append("no")
for i in range(q):
    print(C[i])

