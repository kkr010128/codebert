N,A,B= map(int,input().split())
a=0


if(A==0):
    print(0)
else:
    a=N//(A+B)
    b=N%(A+B)
    if(b<=A):
        print(a*A+b)
    else:
        print((a+1)*A)
    
