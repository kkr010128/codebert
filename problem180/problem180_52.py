#C - Replacing Intege
N,K = map(int, input().split())

for i in range(N):
    if N % K == 0:
        N = 0
        break
    N = N % K
    if abs(N-K) < N:
        N = abs(N-K)
    else :
        break
print(N)