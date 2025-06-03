import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split(" "))
A = list(map(int, input().strip().split(" ")))
A = [0] + A
for i in range(1, N + 1):
    A[i] += A[i - 1]
    A[i - 1] -= i - 1
A[N] -= N

rem_count = {}
rem_count[0] = 1
ans = 0
for i in range(1, N + 1):
    if i - K >= 0:
        rem_count[A[i - K] % K] -= 1
    if A[i] % K in rem_count:
        ans += rem_count[A[i] % K]
        rem_count[A[i] % K] += 1
    else:
        rem_count[A[i] % K] = 1

print(ans)