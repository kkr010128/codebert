r=input().split()
A=int(r[0])
B=int(r[1])
C=int(r[2])
K=int(r[3])
if K<=A:
    print(K)
elif K<=A+B:
    print(A)
else:
    print(2*A-K+B)