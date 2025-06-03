import sys
input = sys.stdin.buffer.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))
A = [a - 1 for a in A]

log_K = 1
while 1 << log_K < K:
    log_K += 1
# print(f'{log_K=}')
D = [[0] * N for _ in range(log_K)]
for i in range(N):
    D[0][i] = A[i]
for k in range(log_K - 1):
    for i in range(N):
        D[k + 1][i] = D[k][D[k][i]]
# print(f'{D=}')

now = 0
k = 0
while K > 0:
    if K & 1:
        now = D[k][now]
    K = K >> 1
    k += 1
print(now + 1)
