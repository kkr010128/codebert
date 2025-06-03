X,K,D = map(int,input().split())
A = abs(X)
ans = 0
if A >= D*K:
    print( A - (D * K))
else :
    e = A//D
    K -= e
    A %= D
    if K%2 == 0:
        print(A)
    else:
        print(D-A)