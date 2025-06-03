def BSort(A,n):
    flag=1
    while flag:
        flag=0
        for i in range(n-1,0,-1):
            if A[i][1]<A[i-1][1]:
                A[i],A[i-1]=A[i-1],A[i]
                flag=1

def SSort(A,n):
    for i in range(n):
        minj=i
        for j in range(i,n):
            if A[j][1]<A[minj][1]:
                minj=j
        A[i],A[minj]=A[minj],A[i]

n = int(input())

A = list(input().split())
B=A[:]

BSort(A,n)
print(' '.join(A))
print('Stable')
SSort(B,n)
print(' '.join(B))

if A==B:
    print('Stable')
else:
    print('Not stable')

