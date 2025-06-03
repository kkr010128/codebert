import sys

def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))

N,K = LI()
A = LI()

ans = []

for i in range(K,N):
    if A[i-K] < A[i]:
        print('Yes')
    else:
        print('No')
