N = int(input())
A = list(int(x) for x in input().split())

ans = 0
for i in range(N):
    if i == N - 1:
        break
    if A[i] > A[i+1]:
        sa = A[i] - A[i+1]
        A[i+1] += sa
        ans = ans + sa

print(ans)
