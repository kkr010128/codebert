N,K,S = map(int,input().split())
A = [10**9]*N
if S != 10**9:
    for i in range(K):
        A[i] = S
else:
    for i in range(N-K):
        A[i] = 10**9-1
print(*A)