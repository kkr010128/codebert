N=int(input())
*X,=sorted(map(int,input().split()))
a=10**9
for p in range(X[0], X[-1]+1):
 a=min(a, sum((n-p)**2 for n in X))
print(a)