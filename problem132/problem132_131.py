import sys
input = sys.stdin.readline
import math


def read():
    N, K = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    return N, K, A


def solve(N, K, A):
    d = [0 for i in range(N+1)]

    for k in range(K):
        for i in range(N):
            d[i] = 0
        
        for i in range(N):
            l = max(0, i-A[i])
            r = min(N, i+1+A[i])
            d[l] += 1
            d[r] -= 1
        
        terminate = True
        v = 0
        for i in range(N):
            v += d[i]
            A[i] = v
            if terminate and A[i] < N:
                terminate = False
        if terminate:
            break         
    print(*[a for a in A])


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
