import sys

MOD = 10**9+7

N,K = map(int, input().split())
A = [[abs(int(x)),1 if int(x)<0 else 0] for x in input().split()]
A.sort(key=lambda x: x[0],reverse=True)
prod = 1
pn = 0
lastn = -1
lastp = -1


for i in range(K):
    if A[i][1] == 1: lastn = i
    else: lastp = i
    pn = (pn + A[i][1]) % 2


if pn == 0:
    if K == N and [0,0] in A:
        print(0)
        sys.exit()
    for i in range(K):
        prod = prod * A[i][0] % MOD
    print(prod)
    sys.exit()

elif pn == 1:
    if K == N:
        if [0,0] in A:
            print(0)
            sys.exit()
        for i in range(N):
            prod = prod * A[i][0] % MOD
        prod = prod * (-1) % MOD
        print(prod)
        sys.exit()
    indp = K
    indn = K
    while indp < N and A[indp][1] == 1:
        indp += 1
    while indn < N and A[indn][1] == 0:
        indn += 1
    if lastp == -1 and indp == N:
        for i in range(K):
            prod = prod * A[-1-i][0] % MOD
        prod = prod * (-1) % MOD
    elif indp == N:
        for i in range(K):
            if i == lastp:
                prod = prod * A[indn][0] % MOD
            else:
                prod = prod * A[i][0] % MOD
    elif lastp == -1 or indn == N:
        for i in range(K):
            if i == lastn:
                prod = prod * A[indp][0] % MOD
            else:
                prod = prod * A[i][0] % MOD
    else:
        for i in range(K):
            if A[indp][0] * A[lastp][0] > A[indn][0] * A[lastn][0]:
                if i == lastn:
                    prod = prod * A[indp][0] % MOD
                else: prod = prod * A[i][0] % MOD
            else:
                if i == lastp:
                    prod = prod * A[indn][0] % MOD
                else:
                    prod = prod * A[i][0] % MOD
    print(prod)