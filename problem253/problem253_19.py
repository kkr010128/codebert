N,A,B=map(int,input().split())
if (A-B)%2==0:
    print(abs(A-B)//2)
else:
    if (A+B)>N:
        print((abs(A-B)-1)//2+(min(N-A,N-B)+1))
    else:
        print((abs(A-B)-1)//2+(min(A-1,B-1)+1))