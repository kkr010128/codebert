n=int(input())
A=100000
for i in range(n):
    A=A*1.05
    if (A%1000!=0):
        A=(A-A%1000)+1000
print(int(A))

