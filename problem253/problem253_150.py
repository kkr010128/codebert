N,A,B = (int(x) for x in input().split())
if (B - A) % 2 == 0:
    print((B-A)//2)
else:
    if B - A == 1:
        if A == 1 or B == N:
            print('1')
        else:
            print('2')
    else:
        if A <= N-B:
            print((A+B-1)//2)
        else:
            print((2*N-A-B+1)//2)