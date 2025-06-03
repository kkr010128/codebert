import sys
input = sys.stdin.readline

N,M = list(map(int,input().split()))
A = sorted(list(map(int,input().split())),reverse = 1)
print('Yes' if A[M-1]>=sum(A)/(4*M) else 'No')
