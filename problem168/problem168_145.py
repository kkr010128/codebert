N, M = map(int, input().split())
A = input().split()

work_days = 0

for i in range(M):
    work_days += int(A[i])

if work_days > N:
    print(-1)
else:
    print(N - work_days)