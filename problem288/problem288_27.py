import math
N=int(input())
M =int(math.sqrt(N))
for i in range(M):
    if N%(M-i)==0:
        K=N//(M-i)
        L=M-i
        break
print(L+K-2)
