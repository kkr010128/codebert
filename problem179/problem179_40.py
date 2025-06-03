N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse = True)
num = 0
for i in A:
    num += i
if A[M-1] >= num/(4*M):
    print('Yes')
else:
    print('No')