n = int(input())
xl = [list(map(int, input().split())) for _ in range(n)]
arms = [[xl[i][0] - xl[i][1], xl[i][0] + xl[i][1]] for i in range(n)]
arms.sort(key=lambda x: x[1])

ans = 1
ne = arms[0][1]
for i in range(n):
    if arms[i][0] >= ne:
        ne = arms[i][1]
        ans += 1
print(ans)
