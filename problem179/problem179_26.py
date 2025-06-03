N,M,*A = map(int, open(0).read().split())
A.sort()
if A[-M]*4*M >= sum(A):
    print('Yes')
else:
    print('No')