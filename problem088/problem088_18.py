N = int(input())
A = list(map(int, input().split()))

ans = 0

for i in range(N - 1):
    if A[i] > A[i + 1]:
        ans += A[i] - A[i + 1]
    A[i + 1] = max(A[i], A[i + 1])

print(ans)
