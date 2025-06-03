X,K,D = map(int, input().split())

X = abs(X)

if X//D > K:
    print(X-(D*K))
    exit()

if (K-X//D)%2:
    print(D-X%D)
else:
    print(X%D)