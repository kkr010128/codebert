N = int(input())
A = [int(i) for i in input().split()]
A = sorted(A, reverse=True)

A += A[1:]
A = sorted(A, reverse=True)

print(sum(A[:N-1]))
