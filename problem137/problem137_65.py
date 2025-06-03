n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

a = [_ab[0] for _ab in ab]
b = [_ab[1] for _ab in ab]
a.sort()
b.sort()

if n % 2 == 1:
    m = a[n // 2]
    M = b[n // 2]
    print(M - m + 1)
else:
    m = (a[n // 2 - 1] + a[n // 2]) / 2
    M = (b[n // 2 - 1] + b[n // 2]) / 2
    print(int((M - m) * 2 + 1))
