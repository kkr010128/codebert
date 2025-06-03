N = int(input())
res = [[0 for _ in range(9)] for _ in range(9)]
for i in range(1, N + 1):
    if i % 10:  res[int(str(i)[0]) - 1][i % 10 - 1] += 1
ans = 0
for i in range(1, N + 1):
    if i % 10:  ans += res[i % 10 - 1][int(str(i)[0]) - 1]
print(ans)