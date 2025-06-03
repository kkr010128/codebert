N, K, S = map(int, input().split())

if S == 10 ** 9:
    res = [S] * K
    res.extend([1] * (N - K))
else:
    res = [S] * K
    res.extend([S + 1] * (N - K))

print(*res)
