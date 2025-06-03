
A,B,M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
X = []
Y = []
C = []
for _ in range(M):
    x,y,c = map(int,input().split())
    X.append(x)
    Y.append(y)
    C.append(c)
ans = min(a) + min(b)
for i in range(M):
    ans = min(ans,a[X[i]-1] + b[Y[i] - 1] - C[i])
print(ans)



