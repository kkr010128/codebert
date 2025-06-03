N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A.sort()
F.sort(reverse=True)

max_a = max(A)
max_f = max(F)

left = 0
right = max_a * max_f

while left <= right:
    x = (left + right) // 2

    sum_ = 0
    for i in range(N):
        if A[i] * F[i] > x:
            sum_ += (A[i] - int(x / F[i]))

    if sum_ > K:
        left = x + 1

    if sum_ <= K:
        right = x - 1


print(left)
