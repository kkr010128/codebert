import bisect
N, M, X = map(int, input().split())
C = [0] * N
A = [0] * N
for i in range(N):
    x = list(map(int, input().split()))
    C[i] = x[0]
    A[i] = [0] * M
    for j in range(M):
        A[i][j] = x[j + 1]
cnt = [0] * (2 ** N)
ans_list = []
for i in range(2 ** N):
    bag = []
    cnt[i] = [0] * M
    for j in range(N):
        if ((i >> j) & 1):
            bag.append(C[j])
            for k in range(M):
                cnt[i][k] += A[j][k]
    cnt[i].sort()
    if bisect.bisect_left(cnt[i], X) == 0:
        ans_list.append(sum(bag))
if ans_list == []:
    print(-1)
else:
    print(min(ans_list))