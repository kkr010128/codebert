n=int(input())
A=list(map(int,input().split()))

m=max(A)

X=[0]*(m+1)

A.sort()

for i in range(n):
    for j in range(A[i]*2,m+1,A[i]):
        X[j]=2
    X[A[i]]+=1


print(X.count(1))