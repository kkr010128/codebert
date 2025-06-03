N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))
A.sort(reverse=True)
F.sort()

C = [None] * N
for i, (a, f) in enumerate(zip(A, F)):
    C[i] = (a * f, f)


def solve(x):
    global K, N
    t = 0
    for c, f in C:
        temp = ((c - x) + f - 1) // f
        t += max(0, temp)
        if t > K:
            result = False
            break
    else:
        result = True
    return result


ok = A[0] * F[N - 1]
ng = -1
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if solve(mid):
        ok = mid
    else:
        ng = mid


print(ok)
