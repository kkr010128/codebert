N = int(input())
A = list(map(int, input().split()))
M = 1000
S = 0
for i in range(N-1):
    if A[i] < A[i+1]:
        S = M // A[i]
        M = M % A[i] + S*A[i+1]
        S = 0
    else:
        pass
print(M)