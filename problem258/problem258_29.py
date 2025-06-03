N=int(input())

if N%2:
    print(0)
else:
    X=0
    Y=N//5
    while Y:
        X+=Y//2
        Y//=5
    print(X)
