#coding: UTF-8

while True:
    N, X = map(int, input().split())
    if N == 0 and X == 0:
        break
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i >= j:
                continue
            c = X - (i + j)
            if c > j and c <= N:
                ans += 1
    print("%d"%(ans))

