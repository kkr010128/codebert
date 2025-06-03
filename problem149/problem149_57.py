N,M,X = map(int,input().split())
C = []
A = []
for i in range(N):
    t = list(map(int,input().split()))
    C.append(t[0])
    A.append(t[1:])

result = -1
# 1 << N 2^N
#There are 2^N possible ways of choosing books
for i in range(1 << N):
    #keep all the understanding level in u
    u = [0]*M
    c = 0
    for j in range(N):
        #move j bit from i
        if (i>>j)&1 == 0:
            continue
        c+= C[j]
        #listwise sum
        for k in range(M):
            u[k] += A[j][k]
        #X is the desired understanding level    
    if all(x >= X for x in u):
        if result == -1:
            result = c
        else:
            result = min(result,c)
            
print(result)