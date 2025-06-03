N = int(input())
A = list(map(int, input().split()))

s = 0

for i in range(1, N):
    if A[i-1] > A[i]:
        s += A[i-1] - A[i]
        A[i] = A[i-1]

print(s)
