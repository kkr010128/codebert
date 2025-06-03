N = int(input())
A = list(map(int, input().split()))
for i in range(1, N):
    A[i] += A[i - 1]
half = A[-1] / 2

A = [abs(i - half) for i in A]
print(int(min(A) * 2))
