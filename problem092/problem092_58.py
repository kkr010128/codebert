X, K, D = map(int, input().split())
X = abs(X)
if X - K * D >= 0:
    print(X - K * D)
    exit()
else:
    n = X // D
    x = X - n * D
    if (K - n) % 2 == 0:
        print(x)
    else:
        print(min(x + D, D - x))
