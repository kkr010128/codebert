A,B,C,K=map(int,input().split())

cnt=0

if A>=K:
    print(K)
else:
    if A+B>=K:
        print(A)
    else:
        if A+B+C<=K:
            print(A-C)
        else:
            print(A-(K-(A+B)))