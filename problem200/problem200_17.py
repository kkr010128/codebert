A,B,M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
x = []
y = []
c = []
for _ in range(M):
    X,Y,Z = map(int,input().split())
    x.append(X)
    y.append(Y)
    c.append(Z)

mini = min(a) + min(b)
for i in range(M):

    rei = a[x[i]-1]
    den = b[y[i]-1]
    coop = c[i]

    if rei + den - coop < mini:
        mini = rei + den - coop

print(mini)
