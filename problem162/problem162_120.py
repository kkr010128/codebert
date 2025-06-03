N, M = map(int, input().split())

diffs = [False] * N

a = 1
b = N
for _ in range(M):
    while True:
        diff0 = b-a
        diff1 = (N+a-b)
        if not diffs[diff0] and not diffs[diff1]:
            break
        b-=1
    diffs[diff0] = True
    diffs[diff1] = True
    print(str(a) + ' ' + str(b))
    a += 1
    b -= 1
    if b-a == (N+a-b):
        b-=1

