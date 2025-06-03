import functools
import operator

n = functools.partial(functools.reduce, operator.mul)
N,K = map(int,input().split())
A = list(map(int,input().split()))
# print(n(A))
for i in range(K,N):
    if A[i-K] < A[i]:
        print("Yes")
    else:
        print("No")
        




