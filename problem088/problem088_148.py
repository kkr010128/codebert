N=int(input())
A = list(map(int,input().split()))
h = 0
for i in range(N-1):
        if max(A[i], A[i+1]) == A[i]:
                h += A[i] - A[i+1]
                A[i+1] = A[i]


print(h)