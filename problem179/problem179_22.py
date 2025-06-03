N, M = map(int, input().split())
A = list(map(int, input().split()))

D = sum(A)
cnt = 0
for i in range(N):
    if A[i] * 4 * M >= D:
        cnt += 1

if cnt >= M:
    print('Yes')
else:
    print('No')