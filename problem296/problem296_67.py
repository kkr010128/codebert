C = {}
S = input().strip()
N = len(S)
K = int(input())
for i in range(N):
    s = S[i]
    if s not in C:
        C[s]=0
    C[s] += 1
if len(C)>1:
    a = 0
    cnt = 1
    for i in range(1,N):
        if S[i]==S[i-1]:
            cnt += 1
        else:
            a += cnt//2
            cnt = 1
    a += cnt//2
    X = S+S
    b = 0
    cnt = 1
    for i in range(1,2*N):
        if X[i]==X[i-1]:
            cnt += 1
        else:
            b += cnt//2
            cnt = 1
    b += cnt//2
    d = b-a
    print(a+d*(K-1))
else:
    A = list(C.items())
    k = A[0][1]
    if k%2==0:
        print((k//2)*K)
    else:
        if K%2==0:
            a = k
            b = 2*k
            d = k
            print(a+d*((K//2)-1))
        else:
            a = k//2
            b = (k*3)//2
            d = b-a
            print(a+d*(K//2))