n = int(input())
d = [[0]*9 for _ in range(9)]
ans = 0

for num in range(1, n+1):
    s = str(num)
    x, y = int(s[0]), int(s[-1])
    if x != 0 and y != 0:
        d[x-1][y-1] += 1

for i in range(9):
    k = -1
    for j in range(9):
        if i == j:
            ans += pow(d[i][j], 2)
            k = 1
        elif k == 1:
            ans += 2*d[i][j]*d[j][i]

print(ans)