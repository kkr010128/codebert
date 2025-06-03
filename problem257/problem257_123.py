N, *A = map(int, open(0).read().split())

cur = 0
for i in range(N):
    if A[i] == cur + 1:
        cur += 1

if cur == 0:
    print(-1)
else:
    print(N - cur)
