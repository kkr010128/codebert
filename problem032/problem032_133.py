n = int(input())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))

for p in range(1,5):
    if p != 4:
        D = 0.0
        for i in range(n):
            D += ((abs(X[i]-Y[i]))**p)
        D = D**(1/p)
        print("{:.6f}".format(D))
    else:
        print("{:.6f}".format(max(abs(x-y)for x,y in zip(X,Y))))

