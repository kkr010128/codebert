N=int(input())
X=list(map(int,input().split()))
Y=[]
for i in range(1,101):
    tot=0
    for n in range(N):
        tot+=(X[n]-i)**2
    Y.append(tot)
print(min(Y))