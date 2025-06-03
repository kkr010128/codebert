N=int(input())

A=[x*y for x in range(1,10) for y in range(1,10)]
A=set(A)

if N in A:
    print("Yes")
else:
    print("No")