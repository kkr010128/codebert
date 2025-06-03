
N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A.sort()
F.sort(reverse=True)

ub = 10 ** 12 + 10
lb = 0
while ub - lb > 1:
    mid = (ub + lb) // 2
    cnt = 0
    for x, y in zip(A, F):
        res = max(0, x * y - mid)
        cnt += -(-res // y)

    if cnt <= K:
        ub = mid
    else:
        lb = mid

if sum(A) <= K:
    print(0)
else:
    print(ub)
