
N = int(input())

x = []
y = []
for i in range(N):
    in1, in2 = list(map(int,input().split()))
    x.append(in1)
    y.append(in2)

#f = [[0]*2 for i in range(N)]
X=[]
Y=[]
for i in range(N):
    #f[i][0] = x[i]-x[i]
    #f[i][1] = x[i]+y[i]
    X.append(x[i]-y[i])
    Y.append(x[i]+y[i])

dam1 = max(X) - min(X)
dam2 = max(Y) - min(Y)
print(max(dam1,dam2))