N, X, T = (int(x) for x in input().split())

if N % X == 0:
    ans = N / X
else:
    ans = N // X + 1

ans = T * ans

print("%d" % ans)
