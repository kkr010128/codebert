N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

cnt = 0
s = 0

for i in range(N):
    s += A[i]

for i in range(N):
    if 4*M*A[i] < s:
        cnt += 1

print(['No', 'Yes'][N - cnt >= M])