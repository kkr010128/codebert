import numpy as np

N = int(input())
X = [[] for _ in range(N)]
L = [[] for _ in range(N)]

for i in range(N):
    X[i], L[i] = map(int, input().split())
    
    
def indexSort(L):
    D = dict(zip(range(len(L)), L))
    E = sorted(D.items(), key=lambda x: x[1])
    F = [e[0] for e in E]
    return F

L1 = [x-l for x, l in zip(X, L)]
L2 = [x+l for x, l in zip(X, L)]


Ind = np.argsort(L2)

Remain = [Ind[0]]
i = 0
while i < len(Ind)-1:
    now = Remain[-1]
    After = Ind[i+1:]

    skip = 0
    for after in After:
        if L2[now] > L1[after]:
#            print(L2[now], L1[after])
            skip += 1
        else:
#            print(after)
            Remain.append(after)
            break
    i += 1 + skip  
print(len(Remain))