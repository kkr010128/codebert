N = int(input())

k, l = divmod(N, 2)

if l == 1:
    print(0)
else:
    cnt = 0
    while k > 1:
        cnt += k // 5
        k //= 5

    print(cnt)

