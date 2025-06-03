N=int(input())
P,Q=108,100

A=(N*Q+P-1)//P
B=((N+1)*Q+P-1)//P-1

if A>B:
    print(":(")
else:
    print(A)
