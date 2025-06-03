X, K, D=(map(int, input().split()))
X=abs(X)

        
N=int(X/D)

if N==0:
    if K%2==0:
        print(X)
    else:
        print(D-X)
else:
    if N>K:
        print(X-K*D)
    elif (K-N)%2==0:
        print(X-N*D)
    else:
        print((N+1)*D-X)