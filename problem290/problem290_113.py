N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))
if sum(A) <= K:
    print(0)
    exit()

def ok(c):
    s = 0
    for i in range(N):
        s += max(0, A[i] - c // F[i])
    return s <= K

A.sort()
F.sort(reverse=True)
l, r = -1, 10 ** 12
while l + 1 < r:
    c = (l + r) // 2
    if ok(c):
        r = c
    else:
        l = c
print(r)
