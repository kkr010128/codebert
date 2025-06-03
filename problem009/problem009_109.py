from functools import lru_cache

@lru_cache(maxsize=None)
def solve(i, count):
    global ans
    global a
    if count >= N:
        return
    if ans[i][0] == -1:
        ans[i][0] = count
    elif ans[i][0] > count:
        ans[i][0] = count

    for x in range(a[i][1]):
        solve(a[i][2 + x] - 1, count + 1)


N = int(input())
a = []
for _ in range(N):
    a.append([int(x) for x in input().split()])

ans = [[-1 for i in range(1)] for j in range(N)]

solve(0, 0)

for i, x in enumerate(ans):
    print(i + 1, *x)




