A,B = list(map(int,input().split()))
N={1:300000,2:200000,3:100000}
if A ==1 and B==1:
    print(1000000)
else:
    try:
        A=N[A]
    except KeyError:
        A=0
    try:
        B=N[B]
    except KeyError:
        B=0
    print(A+B)