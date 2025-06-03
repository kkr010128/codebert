X,K,D = map(int,input().split())
X = abs(X)
if X - D * K >= 0:
    print(X - D * K)
else:
    n = X // D
    X -= n * D
    if (K - n) % 2 == 0:
        print(X)
    else:
        print(abs(X - D))