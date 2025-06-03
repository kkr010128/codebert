n = int(input())
A = sorted(list(map(int, input().split())))
dp = [0] * (10 ** 6 + 10)
for x in A:
    i = 0
    while x + i <= 10 ** 6 + 10:
        if dp[(x-1)] == 2:
            break
        else:
            dp[(x-1) + i] += 1
            i += x

cnt = 0
for x in A:
    if dp[x-1] == 1:
        cnt += 1

print(cnt)