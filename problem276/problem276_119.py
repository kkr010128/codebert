import itertools


N = int(input())
A = [int(x) for x in input().split()]
Acum = list(itertools.accumulate(A))

reg=10**12
for i in range(N):
    reg = min(reg,
             abs(Acum[-1] - Acum[i] * 2))
    
print(reg)