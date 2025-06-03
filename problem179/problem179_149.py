N,M=map(int, input().split())
A=list(map(int, input().split()))
A = sorted(A, reverse=True)

s = sum(A)
th = s * 1/(4*M)

if A[M-1] < th: print('No')
else: print('Yes')