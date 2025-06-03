def foo(x,y,z):
    return x**2 + y**2 + z**2 + x*y + y*z + z*x

N = int(input())

A = [0 for i in range(10050)]

for i in range(1,105):
    for j in range(1,105):
        for k in range(1,105):
            tmp = foo(i,j,k)
            if tmp < 10050:
                A[tmp] += 1

for i in range(1,N+1):
    print(A[i])