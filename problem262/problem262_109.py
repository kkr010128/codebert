from itertools import product
N = int(input())
G = {i:[] for i in range(1,N+1)}
for i in range(1,N+1):
    a = int(input())
    G[i] = [list(map(int,input().split())) for _ in range(a)]
cmax = 0
for z in product((0,1),repeat=N+1):
    if z[0]==0:
        X = []
        for i in range(1,N+1):
            if z[i]==1:
                X.append(i)
        A = []
        B = []
        for i in X:
            for x,y in G[i]:
                if y==1:
                    A.append(x)
                else:
                    B.append(x)
        flag = 0
        for a in A:
            if a not in X:
                flag = 1
                break
        for b in B:
            if b in X:
                flag = 1
                break
        if flag==0:
            cmax = max(cmax,sum(z[1:]))
print(cmax)