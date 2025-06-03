A = list(map(int,input().split()))
if A[0] < A[1]*2:
    print(0)
else:
    print(A[0]-A[1]*2)