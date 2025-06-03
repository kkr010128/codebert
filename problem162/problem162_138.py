N, M = map(int, input().split())

if N % 2 == 1:
    for m in range(1, M + 1):
        print(m, N - m + 1)

count = 1
if N % 2 == 0:
    for m in range(1, M + 1):

        if m <= (N // 2 - 1) // 2:
            start = m
            end = N // 2 - m
            print(start, end)
        else:
            start = N // 2 + count
            end = N - count + 1
            print(start, end)
            count += 1
