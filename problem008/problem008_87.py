count = 0


def solve(i, a, ans):
    global count
    if ans[i][0] == 0:
        count += 1
        ans[i][0] = count

    for x in range(a[i][1]):
        if ans[a[i][2 + x] - 1][0] == 0:
            solve(a[i][2 + x] - 1, a, ans)

    if ans[i][1] == 0:
        count += 1
        ans[i][1] = count


N = int(input())
a = []
for _ in range(N):
    a.append([int(x) for x in input().split()])

ans = [[0 for i in range(2)] for j in range(N)]

for i in range(N):
    if ans[i][0] == 0:
        solve(i, a, ans)

for i, x in enumerate(ans):
    print(i + 1, *x)




