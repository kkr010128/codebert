n = int(input())
xl = [list(map(int, input().split())) for i in range(n)]
l = [[i[0] + i[1], i[0] - i[1]] for i in xl]
l.sort(key=lambda x:x[0])
ans = 0
m = 10 ** 9 * -1
for i in range(n):
    if m <= l[i][1]:
        ans += 1
        m = l[i][0]
print(ans)