N, M = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
thr = -(-sum(A)//(4*M))
for a in A:
    if a >= thr:
        cnt += 1
if cnt >= M:
    print("Yes")
else:
    print("No")
