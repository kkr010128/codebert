X, K, D = map(int,input().split())
res = 0
X = abs(X)
if X >= K * D:
    res = X - K * D
else:
    i = X // D
    j = K - i
    if j % 2 == 0:
        res = X - D * i
    else:
        res = X - D * (i + 1)
print(abs(res))