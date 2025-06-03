MOD = 10 ** 9 + 7
N = int(input())
A = [int(i) for i in input().split()]
sums = [[0] * 3 for _ in range(N + 1)]

ans = 1
for i, a in enumerate(A):
    f = True
    count = 0
    for j in range(3):
        sums[i + 1][j] = sums[i][j]
        if sums[i][j] == a:
            count += 1
            if f:
                sums[i + 1][j] += 1
                f = False
    ans = ans * count % MOD
#print(sums)
print(ans)