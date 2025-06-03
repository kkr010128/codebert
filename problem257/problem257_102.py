N = int(input())
A = [int(a) for a in input().split()]

next_target = 1

idx = []

for i, a in enumerate(A):
    if a == next_target:
        idx.append(i)
        next_target += 1

if not idx:
    print(-1)
else:
    prev = -1
    sum_ = 0

    if idx[-1] != N - 1:
        sum_ += N - (idx[-1] + 1)

    for x in idx:
        sum_ += x - prev - 1
        prev = x

    print(sum_)
