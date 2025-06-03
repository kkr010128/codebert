N=int(input())
A=list(map(int,input().split()))
M=1
if 0 in A:
    print('0')
else:
    for i in range(len(A)):
        M*=A[i]
        if M > 10**18:
            break
    if M > 10**18:
        print('-1')
    else:
        print(int(M))