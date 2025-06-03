N=int(input())
if 1<=N<=100:
    if N%2==1:
        print((N+1)/(2*N))
    elif N%2==0:
        print(1/2)