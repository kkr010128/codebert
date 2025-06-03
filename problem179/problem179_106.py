N,M = (int(x) for x in input().split())
A = [int(x) for x in input().split()]

A = sorted(A,reverse=True)

if A[M-1] * 4 * M >= sum(A):
    print("Yes")
else:
    print("No")
