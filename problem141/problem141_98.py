N = int(input())
A = [int(x) for x in input().split()]
B = [0]*(N+1)

if N == 0:
    if A[0] != 1:
        print(-1)
        exit()
    else:
        print(1)
        exit()
if A[0] != 0:
    print(-1)
    exit()
else:
    B[0] = 1

C = [0]*(N+1)
C[0] = 1
for i in range(1,N+1):
    C[i] = 2*(C[i-1] - A[i-1])
    if C[i] < A[i]:
        print(-1)
        exit()

#print(C)
for i in range(N, 0, -1):
    if i == N:
        B[i] = A[i]
    else:
        B[i] = min(A[i]+B[i+1], C[i])
print(sum(B))
