import itertools

N,K = map(int,input().split())
A = list(map(int,input().split()))

for i in range(K):
    TEMP = [0]*(N+1)
    for j in range(N):
        TEMP[max(0,j-A[j])] +=1
        TEMP[min(N,j+A[j]+1)] -=1
    A = list(itertools.accumulate(TEMP))
    if A[0] == N and A[N-1] == N:
        break

A.pop()
print(*A)