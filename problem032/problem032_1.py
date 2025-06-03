import math
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
tmp = [[0 for i in range(6)] for j in range(n+1)]
absDiff = abs(x[0]-y[0])
tmp[0][3] = tmp[0][0] = absDiff
tmp[0][4] = tmp[0][1] = absDiff ** 2
tmp[0][5] = tmp[0][2] = absDiff ** 3
max = absDiff
for i in range(1, n, 1):
    absDiff = abs(x[i]-y[i])
    tmp[i][0] = absDiff
    tmp[i][1] = absDiff ** 2
    tmp[i][2] = absDiff ** 3
    tmp[i][3] = tmp[i-1][3] + tmp[i][0]
    tmp[i][4] = tmp[i-1][4] + tmp[i][1]
    tmp[i][5] = tmp[i-1][5] + tmp[i][2]
    if absDiff > max:
        max = absDiff
print(tmp[n-1][3])
print(math.sqrt(tmp[n-1][4]))
print(tmp[n-1][5] ** (1/3))
print(max)