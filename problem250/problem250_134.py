X=int(input())
i=2
while i < X:
    if X % i == 0:
        X += 1
        i = 2
    else:
        i += 1
print(X)