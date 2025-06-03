N, M = map(int, input().split())
if N == 1:
    min_range = 0
    max_range = 10
else:
    min_range = 10 ** (N-1)
    max_range = 10 ** N
digits_lis = ['not defined' for _ in range(N+1)]
for _ in range(M):
    s, c = map(int, input().split())
    if digits_lis[s] == 'not defined':
        digits_lis[s] = c
    else:
        if digits_lis[s] != c:
            print('-1')
            break
    if digits_lis[1] == 0 and N != 1:
        print('-1')
        break
else:
    for i in range(min_range, max_range):
        for idx, check in enumerate(digits_lis):
            if check == 'not defined':
                continue
            if (i // 10 ** (N - idx)) % 10 != check:
                break
        else:
            print(i)
            break
