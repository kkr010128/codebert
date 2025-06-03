A=[0 for i in range(45)]
A[0]=1
A[1]=1
for i in range(2,45):
    A[i]=A[i-1]+A[i-2]
B=int(input())
print(A[B])
