n = int(input())

if n < 10:
    print(n)
    quit()

count = [[0] * 10 for _ in range(10)]
for i in range(1, 10):
    count[i][i] = 1

d = 1
for i in range(10, n + 1):
    if i % (d * 10)== 0:
        d *= 10
    h = i // d
    f = i % 10
    count[h][f] += 1

ans = 0
for i in range(10):
    for j in range(10):
        ans += count[i][j] * count[j][i]
print(ans)