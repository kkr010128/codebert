input()
*X,=sorted(map(int,input().split()))
print(min(sum((n-p)**2 for n in X) for p in range(X[0], X[-1]+1)))