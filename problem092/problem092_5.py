X, K, D = [int(v) for v in input().split()]

X = abs(X)
m = X // D
p = K - m if m <= K else 0

if p == 0:
    print(X - (K*D))
else:
    X -= m * D
    if p & 1:
        print(abs(X-D))
    else:
        print(X)