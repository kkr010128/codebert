import itertools
while True:
    n, x = map(int, input().split())
    if n == 0\
    and x == 0:
        break

    a = [i for i in range(1, n+1)]
    b = [i for i in itertools.combinations(a, 3)]
    c = 0
    cnt = 0
    for i in range(len(b)):
        for j in range(3):
            c += b[i][j]
        if c == x:
            cnt += 1
        c = 0
    print(cnt)