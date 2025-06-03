from numba import jit
N, K = map(int, input().split())
A = list(map(int, input().split()))

@jit
def solve(k,n,a):
    for _ in range(k):
        Y = [0]*(n+1)
        for i, x in enumerate(a):
            Y[max(0, i-x)] += 1
            Y[min(n, i+x+1)] -= 1
        for j in range(1, n):
            Y[j] += Y[j-1]
        if a == Y[:-1]:
            break
        a = Y[:-1]
    return a

ans=solve(K,N,A)
print(*ans)