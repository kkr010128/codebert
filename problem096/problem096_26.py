N,D=map(int, input().split())
XY=[map(int, input().split()) for _ in range(N)]
X,Y=[list(i) for i in zip(*XY)]

D2=D**2
K=0

for i in range(0,N):
    S=(X[i])**2+(Y[i])**2
    if D2>=S:
        K+=1

print(K)