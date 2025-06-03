N, K, S = [int(x) for x in input().split()]

result = [S] * K

if S == 10**9:
    ex = 1
else:
    ex = S+1
result.extend([ex] * (N - K))

print(*result)
